package com.ssafy.ieum.Entity;

import lombok.Data;

import javax.persistence.*;

@Entity
@Data
@Table(name = "doginfopredict")
public class Doginfopredicet {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private String id;

    private String dogid;

    private String percent;

    @Column(name = "predicted_breed")
    private String predictedBreed;



}
