package com.sfu.dior.controller;

import com.sfu.dior.dao.ReviewDAO;
import com.sfu.dior.pojo.CompanyReview;
import com.sfu.dior.pojo.Job;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

//@Controller
//public class ReviewController {
//
//    @Autowired
//    private ReviewDAO reviewDAO;
//
//    @RequestMapping("/review")
//    public String listReview(Model m, @RequestParam(value = "compId", defaultValue = "Amazon") String compId) {
//        //test with the url /review?compId=SAP
//        List<CompanyReview> reviews = reviewDAO.findByCompId(compId);
//        m.addAttribute("reviews", reviews);
//        return "review";
//    }
//
//}

@RestController
public class ReviewController {

    @Autowired
    private ReviewDAO reviewDAO;

    @RequestMapping("/review")
    public Map<String, List<CompanyReview>> listReview(Model m, @RequestParam(value = "compId", defaultValue = "Amazon") String compId) {
        //test with the url /review?compId=SAP
        List<CompanyReview> reviews = reviewDAO.findByCompId(compId);
        Map<String, List<CompanyReview>> retData = new HashMap<>();
        retData.put("data", reviews);
        //m.addAttribute("reviews", reviews);
        return retData;
    }

}
