package com.sfu.dior.pojo;

import javax.persistence.*;


public class ConnectionFull {
    private Integer personId;

    private String name;

    private String compId;

    private String title;

    private String country;

    private String province;

    private String city;

    private String link;

    private String education;
    
    private String description;
    
    public ConnectionFull(Object[] objs) {
		// TODO Auto-generated constructor stub
    	setPersonId(Integer.parseInt(objs[0].toString()));
    	setName(objs[1].toString());
    	setCompId(objs[2].toString());
    	setTitle(objs[3].toString());
    	setCity(objs[6].toString());
    	setLink(objs[7].toString());
    	setEducation(objs[8].toString());
    	setDescription(objs[9].toString());
	}
    
    public Integer getPersonId() {
        return personId;
    }

    public void setPersonId(Integer personId) {
        this.personId = personId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCompId() {
        return compId;
    }

    public void setCompId(String compId) {
        this.compId = compId;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }

	public String getEducation() {
		return education;
	}

	public void setEducation(String education) {
		this.education = education;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}
    
    
}
