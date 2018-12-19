package com.sfu.dior.pojo;
import javax.persistence.*;

@Entity
@IdClass(SalaryId.class)
@Table(name = "salary")
public class Salary {
    @Id
    @Column(name = "comp_id")
    private String compId;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "salary_id")
    private int salaryId;

    @Column(name="job_title")
    private String jobTitle;
    
    @Column(name = "avg_salary")
    private Float avgSalary;
    
    @Column(name = "low_salary")
    private Float lowSalary;
    
    @Column(name = "high_salary")
    private Float highSalary;
    
    @Column(name = "currency")
    private String currency;
    
    @Column(name = "job_type")
    private String jobType;
    
    @Column(name="country")
    private String country;
    
    @Column(name="province")
    private String province;
    
    @Column(name = "city")
    private String city;
    
	public String getCompId() {
        return compId;
    }

    public void setCompId(String compId) {
        this.compId = compId;
    }

	public int getSalaryId() {
		return salaryId;
	}

	public void setSalaryId(int salaryId) {
		this.salaryId = salaryId;
	}

	public String getJobTitle() {
		return jobTitle;
	}

	public void setJobTitle(String jobTitle) {
		this.jobTitle = jobTitle;
	}

	public Float getAvgSalary() {
		return avgSalary;
	}

	public void setAvgSalary(Float avgSalary) {
		this.avgSalary = avgSalary;
	}

	public Float getLowSalary() {
		return lowSalary;
	}

	public void setLowSalary(Float lowSalary) {
		this.lowSalary = lowSalary;
	}

	public Float getHighSalary() {
		return highSalary;
	}

	public void setHighSalary(Float highSalary) {
		this.highSalary = highSalary;
	}

	public String getCurrency() {
		return currency;
	}

	public void setCurrency(String currency) {
		this.currency = currency;
	}

	public String getJobType() {
		return jobType;
	}

	public void setJobType(String jobType) {
		this.jobType = jobType;
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

    
}







