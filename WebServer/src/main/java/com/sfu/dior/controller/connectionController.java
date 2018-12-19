package com.sfu.dior.controller;

import com.sfu.dior.dao.ConnectionDAO;
import com.sfu.dior.pojo.ConnectionFull;

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
public class connectionController {
    @Autowired
    private ConnectionDAO connectionDAO;

    Map<String, String> universityShortNameDict = new HashMap<>();
	
    public connectionController() {
		// TODO Auto-generated constructor stub
    	super();
    	universityShortNameDict.put("SFU", "Simon Fraser University");
    	universityShortNameDict.put("UBC", "The University of British Columbia");
    	universityShortNameDict.put("BCIT", "British Columbia Institute of Technology");
    	universityShortNameDict.put("UOT", "University of Toronto");
    	universityShortNameDict.put("SFU", "Simon Fraser University");
	}
    
    @RequestMapping("/alumni")
    public Map<String, List<ConnectionFull>> listConnection(Model model,
    							@RequestParam(value = "compId", defaultValue = "") String compId,
    							@RequestParam(value = "education", defaultValue = "") String education) {
    	
    	if (universityShortNameDict.containsKey(education.toUpperCase())) {
    		education = universityShortNameDict.get(education.toUpperCase());
    	}
        List<Object[]> connections = connectionDAO.getConnectionByCompIdAndEducation(compId, "%"+education+"%");
        
        List<ConnectionFull> alumnis = new ArrayList<>();
        for (Object[] objs : connections) {
        	try {
        		alumnis.add(new ConnectionFull(objs));
        	}catch(Exception e) {
        		
        	}
        }
        Map<String, List<ConnectionFull>> retData = new HashMap<>();
        retData.put("data", alumnis);
        return retData;
    }

}
