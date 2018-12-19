package com.sfu.dior.controller;

import com.sfu.dior.dao.InterviewDAO;
import com.sfu.dior.dao.JobDAO;
import com.sfu.dior.pojo.Interview;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class InterviewController {
    @Autowired
    InterviewDAO interviewDAO;

    @RequestMapping("/interview")
    public Map<String, List<Interview>> listInterview(Model m, @RequestParam(value = "compId", defaultValue = "Amazon") String compId,
                                @RequestParam(value = "jobId",defaultValue = "1") String jobId) throws Exception {
        // test with the url /interview?compId=SAP&jobId=1
        List<Interview> interviews = interviewDAO.findByCompIdAndJobIdOrderByDateDesc(compId, Integer.valueOf(jobId));
        Map<String, List<Interview>> retData = new HashMap<>();
        retData.put("data", interviews);
        
        return retData;
    }
}