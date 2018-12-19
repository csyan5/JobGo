package com.sfu.dior.dao;

import com.sfu.dior.pojo.Connection;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;


public interface AnalysisDAO extends JpaRepository<Connection, Integer> {
    
    @Query(value = "SELECT type, count(1) cnt FROM job WHERE city like ?1 GROUP BY type", nativeQuery=true)
    List<Object[]> getJobTypeCountOverLocation(String location);
    
    @Query(value = "SELECT city, count(1) cnt FROM job WHERE type like ?1 GROUP BY city", nativeQuery=true)
    List<Object[]> getCityCountOverJobType(String jobType);
    
    @Query(value = "SELECT b.bg_name, count(1) cnt FROM connection a, connection_background b WHERE a.person_id = b.person_id AND a.comp_id LIKE ?1 GROUP BY b.bg_name ORDER BY cnt DESC", nativeQuery=true)
    List<Object[]> getUniversityProportionByCompany(String compId);
    
    @Query(value = "SELECT a.comp_id, count(1) cnt FROM connection a, connection_background b WHERE a.person_id = b.person_id AND b.bg_name LIKE ?1 GROUP BY a.comp_id ORDER BY cnt DESC;", nativeQuery=true)
    List<Object[]> getAlumniCountOverCompanyByUniversity(String university);
}
