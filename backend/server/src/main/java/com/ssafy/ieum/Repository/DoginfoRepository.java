package com.ssafy.ieum.Repository;

import com.ssafy.ieum.Entity.Doginfo;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;




@EnableJpaRepositories
public interface DoginfoRepository extends JpaRepository<Doginfo,String> {

    Page<Doginfo> findAll (Pageable pageable);
    Page<Doginfo> findAllByBreed (String breed, Pageable pageable);

    @Query(value = "select * from doginfo where  breed not in ('비숑','시츄','골든리트리버','요크셔테리어','웰시코기','푸들','불독','포메라니안','보더콜리','시바','진도','치와와')",nativeQuery = true)
    Page<Doginfo> findAllByEtc ( Pageable pageable);

}
