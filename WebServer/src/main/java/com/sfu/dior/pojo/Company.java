package com.sfu.dior.pojo;
import javax.persistence.*;

import com.sfu.dior.utils.CommonUtils;

import java.io.Serializable;
import java.sql.Date;

@Entity
//@IdClass(CompanyID.class)
@Table(name = "company")
public class Company {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "comp_id")
    private String compId;


    @Column(name = "website")
    private String webSite;
    @Column(name = "size")
    private String size;
    @Column(name = "type")
    private String type;
    @Column(name = "revenue")
    private String revenue;
    @Column(name = "hq_country")
    private String hqCountry;
    @Column(name = "hq_province")
    private String hqProvince;
    @Column(name = "hq_city")
    private String hqCity;
    @Column(name = "industry")
    private String industry;
    @Column(name = "description")
    private String description;
    @Column(name = "benefit_rating")
    private Float benefitRating;
    @Column(name = "main_benefit")
    private String mainBenefit;
    @Column(name = "logo")//图片以路径存放
    private String logo;
    @Column(name = "founded")
    private Date founded;
    @Column(name = "itv_experience")
    private String itvExperience;
    @Column(name = "itv_obtain_way")
    private String itvObtainWay;
    @Column(name = "itv_difficulty")
    private String itvDifficulty;
    
    public String getCompId() {
        return compId;
    }

    public void setCompId(String compId) {
        this.compId = compId;
    }

    public String getWebSite() {
        return webSite;
    }

    public void setWebSite(String webSite) {
        this.webSite = webSite;
    }

    public String getSize() {
    	if ("".equals(size)) {
    		size = "Unknown";
    	}
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getRevenue() {
        return revenue;
    }

    public void setRevenue(String revenue) {
        this.revenue = revenue;
    }

    public String getHqCountry() {
        return hqCountry;
    }

    public void setHqCountry(String hqCountry) {
        this.hqCountry = hqCountry;
    }

    public String getHqProvince() {
        return hqProvince;
    }

    public void setHqProvince(String hqProvince) {
        this.hqProvince = hqProvince;
    }

    public String getHqCity() {
        return hqCity;
    }

    public void setHqCity(String hqCity) {
        this.hqCity = hqCity;
    }
    
    public String getIndustry() {
        return industry;
    }

    public void setIndustry(String industry) {
        this.industry = industry;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public float getBenefitRating() {
        return benefitRating;
    }

    public void setBenefitRating(float benefitRating) {
        this.benefitRating = benefitRating;
    }

    public String getMainBenefit() {
        return mainBenefit;
    }

    public void setMainBenefit(String mainBenefit) {
        this.mainBenefit = mainBenefit;
    }

    public String getLogo() {
        return logo;
    }

    public void setLogo(String logo) {
        this.logo = logo;
    }

    public Date getFounded() {
    	System.out.println(founded == null);
        return founded;
    }

    public void setFounded(Date founded) {
        this.founded = founded;
    }

	public String getItvExperience() {
		if (itvExperience != null) {
			itvExperience = itvExperience.replaceAll("%", "");
		}
		return CommonUtils.trimSingleQuote(itvExperience);
	}

	public void setItvExperience(String itvExperience) {
		this.itvExperience = itvExperience;
	}

	public String getItvObtainWay() {
		if (itvObtainWay != null) {
			itvObtainWay = itvObtainWay.replaceAll("%", "");
		}
		return CommonUtils.trimSingleQuote(itvObtainWay);
	}

	public void setItvObtainWay(String itvObtainWay) {
		this.itvObtainWay = itvObtainWay;
	}

	public String getItvDifficulty() {
		return itvDifficulty;
	}

	public void setItvDifficulty(String itvDifficulty) {
		this.itvDifficulty = itvDifficulty;
	}
    
}


//@Entity
//@IdClass(PersonID.class)
//public class Person{
//    @Id
//    private int id;
//    @Id
//    private int flag;
//
//   ...
//}
//public class PersonID implements Serializable{
//    int id;
//    int flag;
//}