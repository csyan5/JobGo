
package com.sfu.dior.dao;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;


import com.sfu.dior.pojo.Company;
import com.sfu.dior.pojo.Job;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

//@Repository
public interface CompanyDAO extends JpaRepository<Company, String> {

    @Query("select J from Job J, Company C where C.compId = J.companyId and C.compId = ?1")
    List<Job> findJobsByCompany(String comp_id);
    
    List<Company> findByCompIdContainingOrHqCityContaining(String comp_id, String hq_city);
    List<Company> findAll();
    Company findByCompId(String comp_id);
    //List<Company> findCompaniesByCompId();
//
//    @Query("SELECT U FROM UserDO U ,RoleUserDO RU WHERE U.id = RU.userId AND RU.roleId = :roleId")
//    List<UserDO> findUsersByRole(@Param("roleId") Long roleId);



}
