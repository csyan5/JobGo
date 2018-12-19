package com.sfu.dior.controller;

import java.util.HashMap;
import java.util.List;

import javax.servlet.http.HttpServletRequest;

import org.slf4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.sfu.dior.dao.CompanyDAO;
import com.sfu.dior.dao.ReviewDAO;
import com.sfu.dior.pojo.Company;
import com.sfu.dior.pojo.CompanyReview;
import com.sfu.dior.utils.CommonUtils;

@RestController
public class CompanyController {
	private Logger logger = CommonUtils.getLogger();
	
	@Autowired
    CompanyDAO companyDAO;

	@Autowired
	ReviewDAO reviewDAO;
	
	private HashMap<String, String> benefitLogoDict;
	
	@RequestMapping("/company")
    public ModelAndView company(Model m, @RequestParam(value="compId", defaultValue="") String compId) {
    	logger.info("enter /company");
    	if (!"".equals(compId) && compId!=null) {
    		Company company = companyDAO.findByCompId(compId);
    		if (company != null) {
    			
    			HashMap<String, Object> benefitMap = convertJsonStrToMap(company.getMainBenefit());
    			HashMap<String, Object> itvExperience = convertJsonStrToMap(company.getItvExperience());
    			HashMap<String, Object> itvObtainWay = convertJsonStrToMap(company.getItvObtainWay());
    			String itvDifficulty = company.getItvDifficulty();
    			HashMap<String, Object> itvStat = new HashMap<>();
    			itvStat.put("experience", itvExperience);
    			itvStat.put("obtainWay", itvObtainWay);
    			itvStat.put("difficulty", itvDifficulty);
    			
    			initBenefitLogoDict();
    			m.addAttribute("company", company);
    			m.addAttribute("benefitMap", benefitMap);
    			m.addAttribute("itvStat", itvStat);
    			m.addAttribute("benefitLogoDict", benefitLogoDict);
    			m.addAttribute("avgRatingScore", getRatingScore(compId));
    			return new ModelAndView("company_detail");
    		}
    	}
    	
		List<Company> companyList = companyDAO.findAll();
		m.addAttribute("searchText", "");
		m.addAttribute("companyList", companyList);
		m.addAttribute("companyCount", companyList.size());
		return new ModelAndView("company");
    }
	
	private HashMap<String, String> getRatingScore(String compId){
		List<CompanyReview> reviewList = reviewDAO.findByCompId(compId);
		float[] ratingScores = new float[5];
		
		for (CompanyReview review : reviewList) {
			String[] scores;
			try {
				scores = review.getScore().split("\\|");
			}catch(Exception e) {
				continue;
			}
			
			for (int i=0; i<scores.length && i<5; i++) {
				float score = 0;
				try {
					score = Float.parseFloat(scores[i]);
				}catch(Exception e) {
					score = 0;
				}
				ratingScores[i] += score;
			}
		}
		
		for (int i=0; i<5; i++) {
			ratingScores[i] = ratingScores[i]/reviewList.size()/5*100;
		}
		HashMap<String, String> avgRatingScore = new HashMap<>();
		avgRatingScore.put("workLife",  String.format("%.1f", ratingScores[0]));
		avgRatingScore.put("culture", String.format("%.1f", ratingScores[1]));
		avgRatingScore.put("career", String.format("%.1f", ratingScores[2]));
		avgRatingScore.put("comp", String.format("%.1f", ratingScores[3]));
		avgRatingScore.put("management", String.format("%.1f", ratingScores[4]));
		
		return avgRatingScore;
	}
	
	private HashMap<String, Object> convertJsonStrToMap(String jsonStr){
		HashMap<String, Object> ret;
		logger.info(jsonStr);
		try {
			ret = new Gson().fromJson(new JsonParser().parse(jsonStr), HashMap.class);
		}catch(Exception e) {
			ret = new HashMap<>();
		}
		return ret;
	}
	
	private void initBenefitLogoDict(){
		if (this.benefitLogoDict == null) {
			HashMap<String, String> dict = new HashMap<>();
			dict.put("Life Insurance", "fa-hand-holding-usd");
			dict.put("Health Insurance", "fa-hand-holding-usd");
			dict.put("Pension Plan", "fa-blind");
			dict.put("Retirement Plan", "fa-piggy-bank");
			dict.put("Maternity & Paternity Leave", "fa-hospital-alt");
			dict.put("Vacation & Paid Time Off", "fa-plane");
			dict.put("Employee Discount", "fa-calculator");
			dict.put("Work From Home", "fa-home");
			dict.put("Employee Assistance Program", "fa-handshake");
			dict.put("Job Training & Tuition", "fa-user-graduate");
			dict.put("Private Health/Dental Plan", "fa-tooth");
			dict.put("Extended Health Care", "fa-heartbeat");
			dict.put("Sick Leave", "fa-user-injured fa-procedures");
			dict.put("Flexible Time", "fa-swimmer");
			this.benefitLogoDict = dict;
		}
	}
}
