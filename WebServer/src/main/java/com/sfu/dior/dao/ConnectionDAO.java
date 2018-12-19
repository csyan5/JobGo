package com.sfu.dior.dao;

import com.sfu.dior.pojo.Connection;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;


public interface ConnectionDAO extends JpaRepository<Connection, Integer> {
    List<Connection> findByCompId(String compId);
    
    @Query(value = "SELECT a.*, b.bg_name, b.description FROM connection a, connection_background b where a.person_id = b.person_id and a.comp_id = ?1 and b.bg_name like ?2", nativeQuery=true)
    List<Object[]> getConnectionByCompIdAndEducation(String compId, String education);
}
