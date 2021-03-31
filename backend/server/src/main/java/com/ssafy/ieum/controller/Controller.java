package com.ssafy.ieum.controller;

import com.ssafy.ieum.dto.Response;
import com.ssafy.ieum.service.DogService;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

@RestController
@RequestMapping("/iuem/")
@CrossOrigin(origins = "*")
public class Controller {

    private final DogService dogService ;

    public Controller(DogService dogService) {
        this.dogService = dogService;
    }

    @GetMapping(value = "doginfo/{page}/{size}")
    public Response getDoginfos(@PathVariable("page") Integer page,@PathVariable("size") Integer size){
        System.out.println("getDoginfos");
        Response response;
        try {
            response = new Response("success", "성공", dogService.getalldog(page,size));
        } catch(Exception e){
            return response = new Response("error"," 실패",e.getMessage());
        }
        return response;
    }

    @GetMapping(value = "doginfo/breed/{breedname}/{page}/{size}")
    public Response getDoginfosByBreed(@PathVariable("breedname") String breedname,@PathVariable("page") Integer page,@PathVariable("size") Integer size){
        System.out.println("getDoginfosByBreed");
        Response response;
        try {
            response = new Response("success", "성공", dogService.getDoginfosByBreed(breedname,page,size));
        } catch(Exception e){
            return response = new Response("error"," 실패",e.getMessage());
        }
        return response;
    }
}
