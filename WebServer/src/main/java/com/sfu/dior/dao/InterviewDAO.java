package com.sfu.dior.dao;

import com.sfu.dior.pojo.Interview;
import com.sfu.dior.pojo.InterviewId;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;


public interface InterviewDAO extends JpaRepository<Interview, InterviewId> {
    List<Interview> findByCompIdAndJobIdOrderByDateDesc(String compId, int jobId);
}
