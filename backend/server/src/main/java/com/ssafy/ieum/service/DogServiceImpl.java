package com.ssafy.ieum.service;

import ch.qos.logback.core.net.SyslogOutputStream;
import com.ssafy.ieum.Entity.Doginfo;
import com.ssafy.ieum.Entity.Doginfoimage;
import com.ssafy.ieum.Entity.File;
import com.ssafy.ieum.Repository.DoginfoRepository;
import com.ssafy.ieum.Repository.FileRepository;
import com.ssafy.ieum.dto.Image;
import org.apache.commons.io.IOUtils;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

import javax.sound.midi.Soundbank;
import javax.transaction.Transactional;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.List;

@Service
public class DogServiceImpl implements DogService {

    private final DoginfoRepository doginfoRepository;
    private final FileRepository fileRepository;

    public DogServiceImpl(DoginfoRepository doginfoRepository, FileRepository fileRepository) {
        this.doginfoRepository = doginfoRepository;
        this.fileRepository = fileRepository;
    }

    @Override
    @Transactional
    public List<Doginfo> getalldog(Integer page, Integer size) throws IOException {
        Page<Doginfo> data = doginfoRepository.findAll(PageRequest.of(page, size));
        List<Doginfo> list = data.getContent();
        for (Doginfo info : list) {
            List<String> fileIds = new ArrayList<>();
            for (Doginfoimage doginfoimage : info.getDoginfoimages()) {
                fileIds.add(doginfoimage.getFileId());
            }
            //info.setFiles(filesServe(fileIds));
        }

        return list;
    }

    @Override
    public List<Doginfo> getDoginfosByBreed(String breedname, Integer page, Integer size) {
        Page<Doginfo> data = doginfoRepository.findAllByBreed(breedname, PageRequest.of(page, size));
        List<Doginfo> list = data.getContent();
        for (Doginfo info : list) {
            List<String> fileIds = new ArrayList<>();
            for (Doginfoimage doginfoimage : info.getDoginfoimages()) {
                fileIds.add(doginfoimage.getFileId());
            }
            info.setFiles(filesServe(fileIds));
        }

        for(Doginfo f: list){
            System.out.println(f.getFiles().size());
        }
        return list;
    }

    @Override
    public List<Doginfo> getDoginfosByEctbreed(String breedname, Integer page, Integer size) {
        Page<Doginfo> data = doginfoRepository.findAllByEtc(PageRequest.of(page, size));
        List<Doginfo> list = data.getContent();
        for (Doginfo info : list) {
            List<String> fileIds = new ArrayList<>();
            for (Doginfoimage doginfoimage : info.getDoginfoimages()) {
                fileIds.add(doginfoimage.getFileId());
            }
            info.setFiles(filesServe(fileIds));
        }

        for(Doginfo f: list){
            System.out.println(f.getFiles().size()+f.getBreed());
        }
        return list;
    }

    @Override
    public List<File> filesServe(List<String> filleIds) {
        List<File> images = new ArrayList<>();
        for (String fileId : filleIds) {
                images.add(fileRepository.findById(fileId).get());
        }

        for(File f : images){
            System.out.println( f.getId()+" "+f.getOriginName());
        }

        return images;
    }


//
//    @Override
//    public List<File> filesServe(List<String> fileIds)  {
//        List<File> images = new ArrayList<>();
//        for (String fileId : fileIds) {
//                images.add(fileServe(fileId));
//        }
//        return images;
//    }
//
//    @Override
//    public File fileServe(String fileId)  {
//
//        File image = fileRepository.findById(fileId).get();
//
//
//        String fsl="/";
//
//        StringBuilder path = new StringBuilder();
//
//
//        path.append(fsl).append(image.getPath())
//                .append(fsl).append(image.getSystemName());
//
//        InputStream imgStream = null;
//        try {
//            imgStream = new FileInputStream(path.toString());
//            byte[] imgByteArray = IOUtils.toByteArray(imgStream);
//            imgStream.close();
//            image.setImageBytes(imgByteArray);
//            image.setSize(Integer.toString(imgByteArray.length));
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//
//
//        return image;
//    }

}
