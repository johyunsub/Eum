package com.ssafy.ieum.service;


import com.ssafy.ieum.Entity.Doginfo;
import com.ssafy.ieum.Entity.File;
import org.springframework.data.domain.Page;

import java.io.IOException;
import java.util.List;


public interface DogService {
    List<Doginfo> getalldog(Integer page, Integer size) throws IOException;

    List<File> filesServe(List<String> filleIds);

//    List<File> filesServe(List<String> fileIds) throws IOException;

//    File fileServe(String fileId) throws IOException;

    List<Doginfo> getDoginfosByBreed(String breedname, Integer page, Integer size) ;

    List<Doginfo> getDoginfosByEctbreed(String breedname, Integer page, Integer size);
}
