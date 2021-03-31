package com.ssafy.ieum.Entity;

import lombok.Data;

import javax.persistence.*;

@Entity
@Data
@Table(name = "doginfoimage")
public class Doginfoimage {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private String id;

    private String dogid;

    @Column(name = "file_id")
    private String fileId;
}
