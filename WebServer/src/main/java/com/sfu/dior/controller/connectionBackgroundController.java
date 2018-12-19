package com.sfu.dior.controller;

import com.sfu.dior.dao.BackgroundDAO;
import com.sfu.dior.pojo.ConnectionBackground;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class connectionBackgroundController {
    @Autowired
    private BackgroundDAO backgroundDAO;

    @RequestMapping("/background")
    public List<ConnectionBackground> listBG(@RequestParam(value = "personId", defaultValue = "1") String personId) {
        //test with the url /background?personId=1
        List<ConnectionBackground> allBC = backgroundDAO.findByPersonId(Integer.parseInt(personId));
        return allBC;

    }

}