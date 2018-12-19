package com.sfu.dior.controller;
import com.sfu.dior.dao.JobDAO;
import com.sfu.dior.pojo.Job;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
public class JobController {
    @Autowired
    JobDAO jobDAO;

    @RequestMapping("/job")
    public String listJob(Model m) throws Exception {
//
//        List<Job> jobs = jobDAO.findAll();
//        System.out.println(jobs.get(0).getCity());
//        System.out.println("here----------------------------");
//        System.out.println("here----------------------------");
//        System.out.println("here----------------------------");
//
//        m.addAttribute("jobs", jobs);


        return "job";
    }
}
