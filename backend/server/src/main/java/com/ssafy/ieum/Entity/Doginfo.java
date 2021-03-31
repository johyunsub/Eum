package com.ssafy.ieum.Entity;

import com.ssafy.ieum.dto.Image;
import lombok.Data;

import javax.persistence.*;
import java.util.List;

@Entity
@Data
@Table(name = "doginfo")
public class Doginfo {

    @Id
    private String id;
    private String breed;
    private String location;
    private String url;
    private String phone;
    private String datetime;
    private String sex;

    @OneToMany
    @JoinColumn(name = "dogid")
    private List<Doginfopredicet> doginfopredicet;

    @OneToMany
    @JoinColumn(name = "dogid")
    private List<Doginfoimage> doginfoimages;

    @Transient
    private List<File> files;
}
