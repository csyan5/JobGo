package com.sfu.dior.controller;

import javax.servlet.http.HttpServletRequest;

import org.slf4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import com.sfu.dior.ApplicationConfig;
import com.sfu.dior.service.impl.WordCountServiceImpl;
import com.sfu.dior.utils.CommonUtils;

@RestController
public class ViewController {

	@Autowired
	private WordCountServiceImpl wc;

	@Autowired
	private ApplicationConfig appConfig;
	
	private Logger logger = CommonUtils.getLogger();

	@GetMapping("/")
    public ModelAndView root(Model m) {
    	logger.info("enter index");
    	m.addAttribute("appName",appConfig.getAppName());
    	
        return new ModelAndView("index");
    }
	
    @GetMapping("/index")
    public ModelAndView index(Model m) {
    	logger.info("enter index");
    	m.addAttribute("appName", appConfig.getAppName());
    	
        return new ModelAndView("index");
    }

//    @GetMapping("/job")
//    public ModelAndView job(HttpServletRequest request) {
//    	logger.info("enter job");
//
//    	//logger.info(wc.wordCount("test test mad").toString());
//        return new ModelAndView("job");
//    }
}
