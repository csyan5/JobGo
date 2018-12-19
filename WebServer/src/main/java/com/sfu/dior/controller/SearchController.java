package com.sfu.dior.controller;


import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;
import com.sfu.dior.dao.CompanyDAO;
import com.sfu.dior.dao.JobDAO;
import com.sfu.dior.dao.SalaryDAO;
import com.sfu.dior.pojo.Company;
import com.sfu.dior.pojo.Job;
import com.sfu.dior.utils.CommonUtils;

import org.slf4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class SearchController {
    @Autowired
    JobDAO jobDAO;

    @Autowired
    CompanyDAO companyDAO;

    @Autowired
    SalaryDAO salaryDAO;
    
    private Logger logger = CommonUtils.getLogger();
    
    @RequestMapping("/search")
    public ModelAndView search(Model m, @RequestParam(value="searchType", defaultValue="0") String searchType,
            @RequestParam(value = "searchText", defaultValue = "") String searchText,
            @RequestParam(value = "compId", defaultValue = "") String compId) {
    	logger.info("enter /search");
    	logger.info(searchType);
    	logger.info(searchText);
    	
    	String returnPage = "";
    	if ("0".equals(searchType)) {
    		returnPage = "job";
    		m.addAttribute("searchType", searchType);
    		m.addAttribute("searchText", searchText);
    		m.addAttribute("compId", compId);
    	} else if("1".equals(searchType)) {
    		returnPage = "company";
    		List<Company> companyList = null;
    		if ("".equals(searchText) || "*".equals(searchText) || "null".equals(searchText)) {
    			companyList = companyDAO.findAll();
    		} else {
    			companyList = companyDAO.findByCompIdContainingOrHqCityContaining(searchText, searchText);
    		}
    		m.addAttribute("searchText", searchText);
    		m.addAttribute("companyList", companyList);
    		m.addAttribute("companyCount", companyList.size());
    	} else {
    		returnPage = "index";
    	}
        return new ModelAndView(returnPage);
    }
    
    @RequestMapping("/searchJob")
    public Map<String, List<Job>> listJob(Model m, 
    					@RequestParam(value="searchType", defaultValue="0") String searchType,
                          @RequestParam(value = "searchText", defaultValue = "") String searchText,
                          @RequestParam(value = "compId", defaultValue = "") String compId) throws Exception {
        //searchType == 0 means searching for job
        //searchType == 1 means searching for company
    	
    	List<Job> jobs = null;
    	List<Job> jobPage = null;
    	if ("".equals(compId) || "null".equals(compId)) {
	        if ("".equals(searchText) || "*".equals(searchText) || "null".equals(searchText)) {
	        	jobs = jobDAO.findAll();
	        } else {
	        	jobs = jobDAO.findByTitleContainingOrCompanyIdContainingOrCityContaining(searchText, searchText, searchText);
	        }
    	} else {
    		// from company_detail page, directly use compId to match the job list.
    		jobs = jobDAO.findByCompanyId(compId);
    	}
        
        List<Object[]> itvCountlist = jobDAO.getInterviewCount();
        List<Object[]> salaryCountList = salaryDAO.getSalaryCount();
        
        Map<String, BigInteger> interviewCountMap = new HashMap<>();
        Map<String, Integer> jobTypeSalaryCountMap = new HashMap<>();
        Map<String, Map<String, Integer>> companyJobTypeMap = new HashMap<>();
        
        for (Object[] objs : itvCountlist) {
        	StringBuilder sb = new StringBuilder();
        	sb.append(objs[0]).append(objs[1]);
        	interviewCountMap.put(sb.toString(), (BigInteger) objs[2]);
        }
        
        for (Object[] objs : salaryCountList) {
        	try {
	        	String comp = objs[0].toString();
	        	String[] jobTypes = objs[1].toString().split("\\|");
	        	Integer cnt = ((BigInteger) objs[2]).intValue();
	        	
	        	jobTypeSalaryCountMap = companyJobTypeMap.getOrDefault(comp, new HashMap<>());
	        	
	        	for (String jobType : jobTypes) {
	        		jobType = CommonUtils.convertJobType(jobType);
		        	
		        	jobTypeSalaryCountMap.put(jobType, cnt + jobTypeSalaryCountMap.getOrDefault(jobType, 0));
		        	
		        	companyJobTypeMap.put(comp, jobTypeSalaryCountMap);
	        	}
        	} catch(Exception e) {
        		continue;
        	}
        }
        
        for (Job job : jobs) {
        	String key = job.getCompanyId()+job.getJobId();
        	
        	try {
        		job.setInterviewNum(interviewCountMap.get(key).intValue());
        	}catch(Exception e) {
        		job.setInterviewNum(0);
        	}
        	
    		for (String jobType : job.getType().split("\\|")) {
    			
    			jobType = CommonUtils.convertJobType(jobType);
    			
    			try {
            		if ("Other".equals(jobType)) {
            			job.setSalaryNum(0);
            		} else {
            			job.setSalaryNum(companyJobTypeMap.get(job.getCompanyId()).get(jobType));
            			//job.setSalaryNum(salaryCountMap.get(job.getCompanyId()).intValue());
            		}
        		}catch(Exception e) {
        			job.setSalaryNum(0);
        		}
    		}
        		
        }
        Map<String, List<Job>> retData = new HashMap<>();
        retData.put("data", jobs);
        
        //ObjectWriter ow = new ObjectMapper().writer().withDefaultPrettyPrinter();
        //String jobList = ow.writeValueAsString(retData);
        //m.addAttribute("jobList", jobList);
        return retData;
    }
}
