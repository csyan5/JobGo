package com.sfu.dior.controller;


import com.sfu.dior.RabbitMQ.MessageListenerImpl;
import com.sfu.dior.RabbitMQ.RabbitmqCallBackConfig;
import com.sfu.dior.RabbitMQ.SendCallback;
import com.sfu.dior.dao.AnalysisDAO;
import com.sfu.dior.utils.CommonUtils;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;


@RestController
public class AnalysisController {

    private Logger logger = CommonUtils.getLogger();
    
    @Autowired
    private SendCallback rabbitSender;

    @Autowired
    private RabbitmqCallBackConfig mqConfig;
    
    @Autowired
    private AnalysisDAO analysisDAO;
    
    private List<String> selectedCityList = Arrays.asList(new String[] {
		"Vancouver",
		"Toronto",
		"Ottawa",
		"Calgary",
		"Montreal",
		"Edmonton",
		"Quebec",
		"Waterloo",
		"Seattle",
		"San Francisco",
		"New York"	
	});
    	
    private List<String> selectedJobTypeList = Arrays.asList(new String[] {
		"Data Science",
		"Software Development",
		"Security",
		"UI/UX",
		"Consulting",
		"Supporting",
		"Testing",
		"Management",
		"Administration",
		"Sales",
		"Accountant",
		"Human Resource"
	});
    
    private List<String> selectedCompanyList = Arrays.asList(new String[] {
		"Amazon",
		"RBC",
		"Unbounce",
		"Microsoft",
		"Shopify",
		"Scotiabank",
		"BMO Financial Group",
		"TD",
		"IBM",
		"CIBC",
		"Apple",
		"Deloitte",
		"KPMG",
		"Google",
		"SAP",
		"ICBC"
		//"Facebook"
		//"ATB Financial",
		//"Bell Canada",
		//"Accenture"
	});
    
    private List<String> selectedUniversityList = Arrays.asList(new String[] {
		"Simon Fraser University",
	    "The University of British Columbia",
	    "British Columbia Institute of Technology",
	    "University of Toronto",
	    "McGill University",
	    "Canadian Securities Institute",
	    "University of Victoria",
	    "University of Waterloo",
	    "Concordia University",
	    "York University",
	    "Langara College",
	    "University of Alberta",
	    "Dalhousie University",
	    "Kwantlen Polytechnic University",
	    "Capilano University",
	    "Western University"
	});
    
    @RequestMapping("/analysis")
    public ModelAndView search(Model m, @RequestParam(value="searchType", defaultValue="0") String searchType) {
    	logger.info("enter /analysis");
    	
    	m.addAttribute("selectedCityList", selectedCityList);
    	m.addAttribute("selectedJobTypeList", selectedJobTypeList);
    	m.addAttribute("selectedCompanyList", selectedCompanyList);
    	m.addAttribute("selectedUniversityList", selectedUniversityList);
        return new ModelAndView("analysis");
    }
    
    @RequestMapping("/doAnalysis")
    public Object analyse(Model m,
    					@RequestParam(value="analysisType", defaultValue="") String analysisType,
    					@RequestParam(value="param1", defaultValue="") String param1,
    					@RequestParam(value="param2", defaultValue="") String param2) {
    	
    	Object response = new Object();
    	
    	switch(analysisType) {
    		case "1":
    			//Average Salaries over Job Type
    			StringBuilder jobTypes = new StringBuilder();
    			for (int i=0; i<selectedJobTypeList.size(); i++) {
    				jobTypes.append(selectedJobTypeList.get(i));
    				if (i<selectedJobTypeList.size()-1) {
    					jobTypes.append("|");
    				}
    			}
    			response = sendMsgToRabbitAndWait("1@"+jobTypes.toString());
    			break;
    		case "1.1":
    			//Average Salaries of one Job Type over Location
    			StringBuilder cities = new StringBuilder();
    			for (int i=0; i<selectedCityList.size(); i++) {
    				cities.append(selectedCityList.get(i));
    				if (i<selectedCityList.size()-1) {
    					cities.append("|");
    				}
    			}
    			response = sendMsgToRabbitAndWait("2@"+param1+","+cities.toString());
    			break;
    		case "2":
    			//IT related job proportion in City
    			List<Object[]> objsList = analysisDAO.getJobTypeCountOverLocation("%"+param1+"%");
    			Map<String, Integer> map = new LinkedHashMap<>();
    			for (Object[] objs : objsList) {
    				try {
	    				String jobType = objs[0].toString();
	    				Integer cnt = ((BigInteger) objs[1]).intValue();
	    				String[] types = jobType.split("\\|");
	    				for (String type : types) {
	    					if ("Data Analysis".equals(type) || "Data Science".equals(type) || "Data Mining".equals(type) || "ML/AI".equals(type)) {
	    						type = "Data Science";
	    					} else if ("Software Development".equals(type) || "Operating System".equals(type) || "Database".equals(type)) {
	    						type = "Software Development";
	    					} else if ("Other".equals(type)) {
	    						continue;
	    					}
	    					if (selectedJobTypeList.contains(type)) {
	    						map.put(type, cnt + map.getOrDefault(type, 0));
	    					}
	    				}
    				}catch(Exception e) {
    					continue;
    				}
    			}
    			response = map;
    			break;
    		case "3":
    			objsList = analysisDAO.getCityCountOverJobType("%"+param1+"%");
    			map = new LinkedHashMap<>();
    			for (Object[] objs : objsList) {
    				try {
	    				String city = objs[0].toString();
	    				Integer cnt = ((BigInteger) objs[1]).intValue();
	    				for (String c : selectedCityList) {
	    					if (city.contains(c)) {
	    						map.put(c, cnt + map.getOrDefault(city, 0));
	    					}
	    				}
    				}catch(Exception e) {
    					continue;
    				}
    			}
    			response = CommonUtils.sortMapByValue(map);
    			break;
    		case "4":
    			objsList = analysisDAO.getUniversityProportionByCompany("%"+param1+"%");
    			map = new LinkedHashMap<>();
    			for (int i=0; i<objsList.size(); i++) {
    				Object[] objs = objsList.get(i);
    				try {
	    				String university = objs[0].toString();
	    				Integer cnt = ((BigInteger) objs[1]).intValue();
	    				if ("NULL".equals(university)) {
	    					continue;
	    				}
	    				if (university.contains("SFU")) {
	    					university = "Simon Fraser University";
	    				}
	    				if (cnt>2 || i<=10) {
	    					map.put(university, cnt + map.getOrDefault(university, 0));
	    				}else {
	    					map.put("Other", cnt + map.getOrDefault("Other", 0));
	    				}
    				}catch(Exception e) {
    					continue;
    				}
    			}
    			response = map;
    			break;
    		case "5":
    			objsList = analysisDAO.getAlumniCountOverCompanyByUniversity("%"+param1+"%");
    			map = new LinkedHashMap<>();
    			for (int i=0; i<objsList.size(); i++) {
    				Object[] objs = objsList.get(i);
    				try {
	    				String company = objs[0].toString();
	    				Integer cnt = ((BigInteger) objs[1]).intValue();
	    				if ("NULL".equals(company)) {
	    					continue;
	    				}
	    				if ("ICBC (Insurance Corporation of British Columbia)".equals(company)) {
	    					company = "ICBC";
	    				}
	    				if (cnt>1 || i<=10) {
	    					map.put(company, cnt + map.getOrDefault(company, 0));
	    				}
    				}catch(Exception e) {
    					continue;
    				}
    			}
    			response = CommonUtils.sortMapByValue(map);
    			break;
    		default:
    			break;
    	}
    	
    	try {
			Thread.sleep(500);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	return response;
    }
    
    private String sendMsgToRabbitAndWait(String msg) {
    	MessageListenerImpl listener = mqConfig.exampleListener();
    	listener.reset();
    	
    	rabbitSender.sendMsg(msg);
    	
    	while(!listener.isFinished()) {
    		try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    	}
    
        return listener.getRes();
    }
    
}
