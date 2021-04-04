package com.ssafy.ieum.Entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Entity
@Table
@Data
@NoArgsConstructor
@AllArgsConstructor
public class File {

    @Id
    @GeneratedValue
    private String id;

    @Column(columnDefinition = "float default 0.0")
    private String size;

    @Column(nullable = false)
    private String type;

    @Column(name ="origin_name",nullable = false )
    private String originName;





    @Column
    private byte[] image;
}
