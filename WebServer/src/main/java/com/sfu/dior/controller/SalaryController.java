package com.sfu.dior.controller;

import com.sfu.dior.dao.SalaryDAO;
import com.sfu.dior.pojo.Salary;
import com.sfu.dior.utils.CommonUtils;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class SalaryController {
    @Autowired
    SalaryDAO salaryDAO;

    @RequestMapping("/salary")
    public Map<String, Object> listInterview(Model m, 
	    							@RequestParam(value = "compId", defaultValue = "Amazon") String compId,
	                                @RequestParam(value = "jobTitle", defaultValue = "") String jobTitle,
	                                @RequestParam(value = "jobType", defaultValue = "") String jobType
	    						) throws Exception {
    	
    	List<Salary> salaryList = new ArrayList<>();
    	if ("".equals(jobType) || "Other".equals(jobType)) {
    	} else {
    		String[] types = jobType.split("\\|");
    		for (String type : types) {
    			if ("Data Science".equals(CommonUtils.convertJobType(type))) {
    				
    				salaryList.addAll(salaryDAO.findByCompIdAndJobTypeContaining(compId, "Data Analysis"));
    				salaryList.addAll(salaryDAO.findByCompIdAndJobTypeContaining(compId, "Data Science"));
    				salaryList.addAll(salaryDAO.findByCompIdAndJobTypeContaining(compId, "Data Mining"));
    				salaryList.addAll(salaryDAO.findByCompIdAndJobTypeContaining(compId, "ML/AI"));
    				
    			} else if("Software Development".equals(CommonUtils.convertJobType(type))) {
    				
    				salaryList.addAll(salaryDAO.findByCompIdAndJobTypeContaining(compId, "Software Development"));
    				salaryList.addAll(salaryDAO.findByCompIdAndJobTypeContaining(compId, "Operating System"));
    				salaryList.addAll(salaryDAO.findByCompIdAndJobTypeContaining(compId, "Database"));
    				
    			} else {
    				
    				salaryList.addAll(salaryDAO.findByCompIdAndJobTypeContaining(compId, type));
    				
    			}
    		}
    	}
        
        
        Float avg = new Float(0);
        Float low = new Float(999999999999999.9);
        Float high = new Float(0);
        for (Salary salary : salaryList) {
        	avg += salary.getAvgSalary();
        	low = Math.min(low, salary.getLowSalary());
        	high = Math.max(high, salary.getHighSalary());
        }
        avg = salaryList != null && salaryList.size()>0 ? avg/salaryList.size() : 0;
        
        Map<String, Object> retData = new HashMap<>();
        retData.put("avg", avg);
        retData.put("range", low.toString()+" - "+high.toString());
        retData.put("salaryList", salaryList);
        
        return retData;
    }
}