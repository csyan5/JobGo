package com.sfu.dior.dao;

import com.sfu.dior.pojo.Job;
import com.sfu.dior.pojo.JobId;
import com.sfu.dior.pojo.JobWithDescription;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;


public interface JobDAO extends JpaRepository<Job, JobId> {
    List<Job> findAll();
    List<Job> findByCompanyId(String compId);
    List<Job> findByTitleContainingOrCompanyIdContainingOrCityContaining(String title, String companyId, String city);

    @Query(value = "SELECT comp_id, job_id, count(1) cnt FROM interview GROUP BY comp_id, job_id", nativeQuery=true)
    List<Object[]> getInterviewCount();
    
    @Query("select j from JobWithDescription j where j.companyId = ?1 and j.jobId = ?2")
    JobWithDescription findDescription(String compId, int jobId);
}
