package com.sfu.dior.controller;


import com.sfu.dior.dao.CompanyDAO;
import com.sfu.dior.dao.JobDAO;
import com.sfu.dior.pojo.Job;
import com.sfu.dior.pojo.JobWithDescription;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DescriptionController {
    @Autowired
    private JobDAO jobDAO;

    @RequestMapping("/description")
    public String getDescription(@RequestParam(value = "compId", defaultValue = "SAP") String compId, @RequestParam(value = "jobId", defaultValue = "0") String jobId){
        JobWithDescription job = jobDAO.findDescription(compId, Integer.parseInt(jobId));
        return job.getDescription();
    }
}
