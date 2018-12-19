package com.sfu.dior.dao;

import com.sfu.dior.pojo.CbId;
import com.sfu.dior.pojo.ConnectionBackground;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface BackgroundDAO extends JpaRepository<ConnectionBackground, CbId> {
    List<ConnectionBackground> findByPersonId(int personId);
}