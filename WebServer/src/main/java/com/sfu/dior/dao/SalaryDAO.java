package com.sfu.dior.dao;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.sfu.dior.pojo.JobWithDescription;
import com.sfu.dior.pojo.Salary;
import com.sfu.dior.pojo.SalaryId;

public interface SalaryDAO extends JpaRepository<Salary, SalaryId> {
    List<Salary> findByCompIdAndJobTypeContaining(String compId, String jobType);
    
    @Query(value = "SELECT comp_id, job_type, count(1) cnt FROM salary GROUP BY comp_id, job_type", nativeQuery=true)
    List<Object[]> getSalaryCount();
}