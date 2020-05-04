package com.financialTransactionAnalyzer.dataProcessor.Controllers;

import java.io.IOException;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DataController {
	
	// Upload csv, which runs py script and dumps into mysql
	@RequestMapping("dataUpload")
    public String dataUpload() throws IOException {
		
		
		
        return "Processed!";
    }

}
