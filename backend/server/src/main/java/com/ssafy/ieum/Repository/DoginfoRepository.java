package com.ssafy.ieum.Repository;

import com.ssafy.ieum.Entity.Doginfo;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;




@EnableJpaRepositories
public interface DoginfoRepository extends JpaRepository<Doginfo,String> {

    Page<Doginfo> findAll (Pageable pageable);
    Page<Doginfo> findAllByBreed (String breed, Pageable pageable);

}
