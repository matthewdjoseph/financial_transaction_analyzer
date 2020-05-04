package com.financialTransactionAnalyzer.dataProcessor.Controllers;

import java.io.IOException;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DataController {
	
	// Upload csv, which runs py script and dumps into mysql
	@RequestMapping("dataUpload")
    public String dataUpload() throws IOException {
		
		// Script not launching
		String fetching = "python " + "C:\\Users\\mdjos\\workspaces\\financial_transaction_analyzer\\python data processing\\bigdata.py";
		String[] commandToExecute = new String[]{"cmd.exe", "/c start", fetching};
		Runtime.getRuntime().exec(commandToExecute);
		
        return "Processed!";
    }

}
