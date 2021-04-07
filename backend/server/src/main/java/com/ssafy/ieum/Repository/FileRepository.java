package com.ssafy.ieum.Repository;


import com.ssafy.ieum.Entity.File;
import org.springframework.data.jpa.repository.JpaRepository;

public interface FileRepository extends JpaRepository<File,String> {



}