package com.sfu.dior.dao;

import com.sfu.dior.pojo.CompanyReview;
import com.sfu.dior.pojo.CompanyReviewId;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ReviewDAO extends JpaRepository<CompanyReview, CompanyReviewId> {
    List<CompanyReview> findByCompId(String compId);
}
