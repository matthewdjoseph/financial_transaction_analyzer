package com.financialTransactionAnalyzer.dataProcessor.server;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

import com.financialTransactionAnalyzer.dataProcessor.Controllers.DataController;

@SpringBootApplication
@ComponentScan(basePackageClasses = DataController.class)
public class SpringBootServer {

	public static void main(String[] args) {
		SpringApplication.run(SpringBootServer.class, args);
	}

}
