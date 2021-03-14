package com.ssafy.ieum.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/iuem")
@CrossOrigin
public class Controller {

    @GetMapping
    public String test(){
        return "test";
    }
}
