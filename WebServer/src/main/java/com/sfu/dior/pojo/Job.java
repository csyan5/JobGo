package com.sfu.dior.pojo;
import javax.persistence.*;

@Entity
@IdClass(JobId.class)
@Table(name = "job")
public class Job {
    @Id
    @Column(name = "comp_id")
    private String companyId;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "job_id")
    private int jobId;

    @Column(name="title")
    private String title;
    @Column(name="country")
    private String country;
    @Column(name="province")
    private String province;
    @Column(name = "city")
    private String city;
    @Column(name = "avg_salary")
    private String avgSalary;
    @Column(name = "low_salary")
    private String lowSalary;
    @Column(name = "high_salary")
    private String highSalary;
    @Column(name = "fulltime")
    private String fullTime;
    @Column(name = "type")
    private String type;
    @Column(name = "industry")
    private String industry;
    @Column(name = "apply_link")
    private String applyLink;
    
    private Integer salaryNum;
    
    private Integer interviewNum;
    
    public Integer getSalaryNum() {
    	return salaryNum;
    }
    
    public void setSalaryNum(Integer salaryNum) {
    	this.salaryNum = salaryNum;
    }
    
    public Integer getInterviewNum() {
		return interviewNum;
	}

	public void setInterviewNum(Integer interviewNum) {
		this.interviewNum = interviewNum;
	}

	public String getCompanyId() {
        return companyId;
    }

    public void setCompanyId(String companyId) {
        this.companyId = companyId;
    }

    public int getJobId() {
        return jobId;
    }

    public void setJobId(int jobId) {
        this.jobId = jobId;
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

    public String getAvgSalary() {
        return avgSalary;
    }

    public void setAvgSalary(String avgSalary) {
        this.avgSalary = avgSalary;
    }

    public String getLowSalary() {
        return lowSalary;
    }

    public void setLowSalary(String lowSalary) {
        this.lowSalary = lowSalary;
    }

    public String getHighSalary() {
        return highSalary;
    }

    public void setHighSalary(String highSalary) {
        this.highSalary = highSalary;
    }

    public String getFullTime() {
        return fullTime;
    }

    public void setFullTime(String fullTime) {
        this.fullTime = fullTime;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getIndustry() {
        return industry;
    }

    public void setIndustry(String industry) {
        this.industry = industry;
    }

    public String getApplyLink() {
        return applyLink;
    }

    public void setApplyLink(String applyLink) {
        this.applyLink = applyLink;
    }
}







