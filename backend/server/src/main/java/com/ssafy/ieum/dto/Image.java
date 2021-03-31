package com.ssafy.ieum.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;


@Data
@NoArgsConstructor
@AllArgsConstructor
public class Image {

    private int id;
    private String path;
    private String originName;
    private String systemName;
    private int size;
    private String type;
    private byte[] imageBytes;

}
