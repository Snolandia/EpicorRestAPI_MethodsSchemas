import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.RPT.ProcessPaymentSvc
// Description: Initializes a new class of "ProcessPaymentSvc" />.
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GenerateBankExportFile
   Description: GetBankExportFile.
   OperationID: GenerateBankExportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateBankExportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateBankExportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateBankExportFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GenerateBankExportFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewProcessPayment
   Description: Call this method instead of GetNewParameters.
This method has the functionality of GetNewParameters and it takes
GroupID as input so it can fill the ProcessPaymentDataset with
relevant data for the GroupID.
The BL determines whether its a Start / ReStart process payment and sends the data accordingly.
   OperationID: GetNewProcessPayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProcessPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProcessPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewProcessPayment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GetNewProcessPayment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewProcessPaymentForSingleRemitAdvice
   Description: Call this method instead of GetNewParameters when printing a remittance advice for a single check.
This method has the functionality of GetNewParameters and it takes
HeadNum as input so it can fill the ProcessPaymentDataset with
relevant data for the CHeck.
   OperationID: GetNewProcessPaymentForSingleRemitAdvice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProcessPaymentForSingleRemitAdvice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProcessPaymentForSingleRemitAdvice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewProcessPaymentForSingleRemitAdvice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GetNewProcessPaymentForSingleRemitAdvice", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankAcctID
   Description: Call method when the user changes the Bank account in Process Payment.
   OperationID: OnChangeBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankAcctID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/OnChangeBankAcctID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCheckDate
   Description: Call method when the over rides the check # in Process Payment.
   OperationID: OnChangeCheckDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCheckDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCheckDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCheckDate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/OnChangeCheckDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLoadedCheckNum
   Description: Call method when the over rides the check # in Process Payment.
   OperationID: OnChangeLoadedCheckNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLoadedCheckNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLoadedCheckNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLoadedCheckNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/OnChangeLoadedCheckNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankExportFileName
   Description: Call method when the BankExportFileName changes
   OperationID: OnChangeBankExportFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankExportFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankExportFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankExportFileName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/OnChangeBankExportFileName", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OverwriteFileWarning
   Description: Purpose:
Parameters:  none
Notes:
<param name="inFileName">File Name</param><param name="vWarningMessage">Overwrite file warning message.</param>
   OperationID: OverwriteFileWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OverwriteFileWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OverwriteFileWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OverwriteFileWarning(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/OverwriteFileWarning", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method paymentGroupingPO3
   Description: Process group for PO3
   OperationID: paymentGroupingPO3
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/paymentGroupingPO3_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/paymentGroupingPO3_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_paymentGroupingPO3(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/paymentGroupingPO3", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreRunDirect
   Description: This method is called when printing or generating and contains extra logic which is run before RunDirect.
   OperationID: PreRunDirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreRunDirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreRunDirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreRunDirect(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/PreRunDirect", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RunProcessPayment
   Description: Process Payments.
   OperationID: RunProcessPayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunProcessPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunProcessPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunProcessPayment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/RunProcessPayment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReStartProcessPayment
   Description: Process Payments.
   OperationID: ReStartProcessPayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReStartProcessPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReStartProcessPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReStartProcessPayment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/ReStartProcessPayment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TestGroupProcessing
   Description: Test Group Processing
   OperationID: TestGroupProcessing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestGroupProcessing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestGroupProcessing_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestGroupProcessing(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/TestGroupProcessing", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateElecIntFile
   Description: Validate Electronic Interface File
   OperationID: ValidateElecIntFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateElecIntFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateElecIntFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateElecIntFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/ValidateElecIntFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method validateProcessPaymentParam
   Description: Purpose:     Common validations used by ReStartProcessPayment and ProcessPayment.
Parameters:  none
Notes:
   OperationID: validateProcessPaymentParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/validateProcessPaymentParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateProcessPaymentParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_validateProcessPaymentParam(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/validateProcessPaymentParam", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescrList
   Description: Purpose:     Get code descriptions list
Parameters:  none
Notes:
   OperationID: GetCodeDescrList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescrList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescrList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GetCodeDescrList", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method getCurrencyID
   Description: Purpose:     Get the currency id
Parameters:  none
Notes:
   OperationID: getCurrencyID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getCurrencyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getCurrencyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getCurrencyID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/getCurrencyID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method getEFTProductionNumber
   Description: Purpose:     Get Production Number for EFT from patch field.
Parameters:  The Product Number is between 1 - 9 for each day and restarts after 9.
If this method is being called by a validation process, the inUpdate should
be assigned to false until ready to post.
Notes:
   OperationID: getEFTProductionNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getEFTProductionNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getEFTProductionNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getEFTProductionNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/getEFTProductionNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method getNextECheckNum
   Description: Purpose:     Get the last payment number for the specified bank account for Electronic payment
Parameters:  none
Notes:
   OperationID: getNextECheckNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getNextECheckNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getNextECheckNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getNextECheckNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/getNextECheckNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method getStartCheckNum
   Description: Purpose:     Get the last payment number for the specified bank account,
increment by 1 to display the starting payment number.
Parameters:  none
Notes:
   OperationID: getStartCheckNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getStartCheckNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getStartCheckNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_getStartCheckNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/getStartCheckNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSortByList
   Description: Returns a list of SortBy options
   OperationID: GetSortByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSortByList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GetSortByList", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method validateNegativePaymentExist
   Description: Purpose:     Validate a negative payment exists
Parameters:  none
Notes:
   OperationID: validateNegativePaymentExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/validateNegativePaymentExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateNegativePaymentExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_validateNegativePaymentExist(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/validateNegativePaymentExist", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockRecord
   Description: Create the document lock
   OperationID: LockRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockRecord(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/LockRecord", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsLocked
   Description: Check is a document lock is in place
   OperationID: IsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsLocked(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/IsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsGenerated
   Description: Check if the payment has already been generated
   OperationID: IsGenerated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsGenerated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsGenerated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsGenerated(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/IsGenerated", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTokenList
   Description: Returns a comma separated list of valid tokens for the given datatype.
   OperationID: Get_GetTokenList
      @param tokenDataType Desc: Type of token for which you want the list of valid values. Valid Types are; Date, FiscalPeriod, FiscalYear   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetTokenList(tokenDataType:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tokenDataType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tokenDataType=" + tokenDataType
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GetTokenList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTokenValue
   Description: Returns a token list of values based on a type that is passed in.
   OperationID: Get_GetTokenValue
      @param pcValue Desc: Type of token   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetTokenValue(pcValue:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof pcValue!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pcValue=" + pcValue
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GetTokenValue" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRptArchiveList
   Description: Returns a sub-delimited list of valid archive codes/descriptions.
   OperationID: GetRptArchiveList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRptArchiveList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRptArchiveList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GetRptArchiveList", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SubmitToAgent
   Description: Submits this report to a System Agent. The system agent will run the task based on the defined schedule.
   OperationID: SubmitToAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitToAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitToAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitToAgent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/SubmitToAgent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaults
   Description: Use to get the current parameter defaults that the user has established for this report.
Note: This is automatically run as part of the GetNewParameters method.
In cases where the ParamSetID would be blank (this is most cases) you would not need to call this method.
It is provided to provide the ability to get the defaults after the user has enter a value into the field
designated as ParamSetID.
As is the case in GLFinancial Reports the GLFinancialParam.GLReportID is used as the ParamSetID field.
Another possible use would be to Reset the screen to default values.
   OperationID: GetDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GetDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewParameters
   Description: Creates a new (parameter record) in the dataset.
Note: A parameter dataset should never contain more than one record.
   OperationID: Get_GetNewParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetNewParameters(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GetNewParameters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetParamsFromAgent
   Description: Gets existing parameter values from the Task Agent and returns them in the in the dataset.
Note: Parameters are stored as individual fields in the database. This method is
used to retrieve those values and return them in the specific dataset.
   OperationID: Get_GetParamsFromAgent
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamsFromAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetParamsFromAgent(agentID:string, agentSchedNum:string, agentTaskNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof agentID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "agentID=" + agentID
   }
   if(typeof agentSchedNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "agentSchedNum=" + agentSchedNum
   }
   if(typeof agentTaskNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "agentTaskNum=" + agentTaskNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GetParamsFromAgent" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetParamTaskDef
   Description: Use to get the specified ProcessSet Task defaults that the user has established for this report.
It is provided to provide the ability to get the defaults after the user has enter a value into the field
designated as ParamSetID.
   OperationID: GetParamTaskDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetParamTaskDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamTaskDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetParamTaskDef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/GetParamTaskDef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveDefaults
   Description: Use to remove the current parameter defaults that the user has established for this report.
   OperationID: RemoveDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/RemoveDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RunDirect
   Description: Use to run the process directly from the client instead of submitting to a System Agent.
   OperationID: RunDirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunDirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunDirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunDirect(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/RunDirect", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveDefaults
   Description: Use to save the current parameters as the users defaults for this report
   OperationID: SaveDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/SaveDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveProcessTask
   Description: Use to save the current parameters as the users defaults for this report
<param name="maintProgram">UI Maintenance program </param><param name="ds" />
   OperationID: SaveProcessTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveProcessTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveProcessTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveProcessTask(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/SaveProcessTask", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_ProcessPaymentParamRow{
   Company:string,
   CheckDate:string,
   FiscalYear:number,
   FiscalPeriod:number,
   BankAcctID:string,
   LastUsedCheckNum:number,
   BankExportFileName:string,
   ElecPayment:boolean,
      /**  Indicates wether its a restart payment or a process payment.  */  
   ReStartProcessPayment:boolean,
   GroupID:string,
      /**  Last good check number printed.  Used in re-process payments  */  
   LastGoodCheckNum:number,
   BankAcctIdDescription:string,
   BankAcctIdBankName:string,
   OverridePayment:boolean,
      /**  Can be C for checks, B for both or R for remit.  */  
   FormsToGenerate:string,
      /**  enable forms prompt.  */  
   EnableFormsPrompt:boolean,
   FiscalYearSuffix:string,
   SortBy:string,
   LoadedCheckNum:number,
      /**  Determine if the payment method is Check Printing.  */  
   CheckPrinting:boolean,
      /**  Suppliers filtering list. Only for Remittance Advice reprinting.  */  
   SupplierList:string,
      /**  Payments filtering list. Only for Remittance Advice reprinting.  */  
   PaymentList:string,
      /**  Remmitance Advice reprinting  */  
   RemittanceReprint:boolean,
   ElecPaymentGen:boolean,
   BankExportDisplayFileName:string,
   MICRCheck:boolean,
      /**  Process Type  */  
   ProcessType:string,
   SupplierIDList:string,
   HeadNum:number,
   SysRowID:string,
   AutoAction:string,
   PrinterName:string,
   AgentSchedNum:number,
   AgentID:string,
   AgentTaskNum:number,
   RecurringTask:boolean,
   RptPageSettings:string,
   RptPrinterSettings:string,
   RptVersion:string,
   ReportStyleNum:number,
   WorkstationID:string,
   TaskNote:string,
   ArchiveCode:number,
   DateFormat:string,
   NumericFormat:string,
   AgentCompareString:string,
   ProcessID:string,
   ProcessCompany:string,
   ProcessSystemCode:string,
   ProcessTaskNum:number,
   DecimalsGeneral:number,
   DecimalsCost:number,
   DecimalsPrice:number,
   GlbDecimalsGeneral:number,
   GlbDecimalsCost:number,
   GlbDecimalsPrice:number,
   FaxSubject:string,
   FaxTo:string,
   FaxNumber:string,
   EMailTo:string,
   EMailCC:string,
   EMailBCC:string,
   EMailBody:string,
   AttachmentType:string,
   ReportCurrencyCode:string,
   ReportCultureCode:string,
   SSRSRenderFormat:string,
   UIXml:string,
   PrintReportParameters:boolean,
   SSRSEnableRouting:boolean,
   DesignMode:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProcessPaymentTableset{
   ProcessPaymentParam:Erp_Tablesets_ProcessPaymentParamRow[],
   ReportStyle:Erp_Tablesets_ReportStyleRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ReportStyleRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Report ID  */  
   ReportID:string,
      /**  Report Style Number  */  
   StyleNum:number,
      /**  Report Style Description  */  
   StyleDescription:string,
      /**  Foreign key to the ReportType table which defines the type of report (Crystal, EpiForms, etc)  */  
   RptTypeID:string,
      /**  Program which performs the actual printing  */  
   PrintProgram:string,
      /**  additonal options/settings required by specfic PrintProgram  */  
   PrintProgramOptions:string,
      /**  Foreign Key to RptDef table.  */  
   RptDefID:string,
      /**   Delimited list of company id's that can use this ReportStyle.
Blank = All Companies. This field will not be overlaid during release upgrades.
This field is not intended to be directly updatable. Instead it is exposed to the UI in a separate table (ReportCompany) which is not a physical db table. All Companies are created in ReportCompany. If in the CompanyList, then ReportCompany.ValidStyle = Yes
Delimeter character is global LIST-DELIM value  (~)  */  
   CompanyList:string,
      /**  This is a Crystal Server Num that is defined in CrystalServer table.  */  
   ServerNum:number,
      /**   Specifies an output location for Bartender and Outbound EDI Reports to override the default locations:
mfgsysdata\Bartender
mfgsysdata\EDI  */  
   OutputLocation:string,
      /**  Field to save if file is going to be exported in txt o xml format  */  
   OutputEDI:string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RptCriteriaSetID  */  
   RptCriteriaSetID:string,
      /**  RptStructuredOutputDefID  */  
   RptStructuredOutputDefID:string,
      /**  StructuredOutputEnabled  */  
   StructuredOutputEnabled:boolean,
      /**  RequireSubmissionID  */  
   RequireSubmissionID:boolean,
      /**  AllowResetAfterSubmit  */  
   AllowResetAfterSubmit:boolean,
      /**  CertificateID  */  
   CertificateID:string,
      /**  Language  */  
   LangNameID:string,
      /**  Culture Format  */  
   FormatCulture:string,
      /**  StructuredOutputCertificateID  */  
   StructuredOutputCertificateID:string,
      /**  StructuredOutputAlgorithm  */  
   StructuredOutputAlgorithm:string,
      /**  True if any data source for this report data definition is related to a BAQ or EI. False in other case.  */  
   HasBAQOrEI:boolean,
      /**  Flag to indicate if this report style record has an enabled routing rule.  */  
   RoutingRuleEnabled:boolean,
      /**  Digital cert for signing is an All Company cert.  */  
   CertificateIsAllComp:boolean,
      /**  Indicates the certificate is a system cert.  */  
   CertificateIsSystem:boolean,
      /**  Certificate expiration date.  */  
   CertExpiration:string,
      /**  Report Style status (from HealthCheck).It indicates if there are issues in the report style: 0 - OK, 1 - Missing RDL, etc.  */  
   Status:number,
      /**  Report Style status message (from HealthCheck).It is a more detailed message with  issues found, ie. the names of the missing RDL files.  */  
   StatusMessage:string,
   RptDefSystemFlag:boolean,
   LangNameIDDescription:string,
   IsBAQReport:boolean,
   StructuredOutputCertificateIsAllComp:boolean,
   StructuredOutputCertificateIsSystem:boolean,
   StructuredOutputCertificateExpirationDate:string,
   AllowGenerateEDI:boolean,
   BitFlag:number,
   ReportRptDescription:string,
   RptDefRptDescription:string,
   RptTypeRptTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ds
   */  
export interface GenerateBankExportFile_input{
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface GenerateBankExportFile_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}
}

export interface GetCodeDescrList_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface GetDefaults_input{
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface GetDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}
}

export interface GetNewParameters_output{
   returnObj:Erp_Tablesets_ProcessPaymentTableset[],
}

   /** Required : 
      @param headNum
   */  
export interface GetNewProcessPaymentForSingleRemitAdvice_input{
      /**  Check Head Num  */  
   headNum:number,
}

export interface GetNewProcessPaymentForSingleRemitAdvice_output{
   returnObj:Erp_Tablesets_ProcessPaymentTableset[],
}

   /** Required : 
      @param pcGroupID
      @param formCalled
   */  
export interface GetNewProcessPayment_input{
      /**  AP Check Group ID  */  
   pcGroupID:string,
      /**  Which form called process payments.  */  
   formCalled:string,
}

export interface GetNewProcessPayment_output{
   returnObj:Erp_Tablesets_ProcessPaymentTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetParamTaskDef_input{
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface GetParamTaskDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}
}

   /** Required : 
      @param agentID
      @param agentSchedNum
      @param agentTaskNum
   */  
export interface GetParamsFromAgent_input{
   agentID:string,
   agentSchedNum:number,
   agentTaskNum:number,
}

export interface GetParamsFromAgent_output{
   returnObj:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface GetRptArchiveList_output{
   returnObj:string,
}

export interface GetSortByList_output{
parameters : {
      /**  output parameters  */  
   sortbylist:string,
}
}

   /** Required : 
      @param tokenDataType
   */  
export interface GetTokenList_input{
      /**  Type of token for which you want the list of valid values. Valid Types are; Date, FiscalPeriod, FiscalYear  */  
   tokenDataType:string,
}

export interface GetTokenList_output{
   returnObj:string,
}

   /** Required : 
      @param pcValue
   */  
export interface GetTokenValue_input{
      /**  Type of token  */  
   pcValue:string,
}

export interface GetTokenValue_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   pcTokenValue:string,
}
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

   /** Required : 
      @param company
      @param groupID
   */  
export interface IsGenerated_input{
   company:string,
   groupID:string,
}

export interface IsGenerated_output{
   returnObj:boolean,
}

   /** Required : 
      @param company
      @param groupID
      @param relatedToFile
      @param lockStatus
   */  
export interface IsLocked_input{
   company:string,
   groupID:string,
   relatedToFile:string,
   lockStatus:string,
}

export interface IsLocked_output{
   returnObj:boolean,
}

   /** Required : 
      @param groupID
   */  
export interface LockRecord_input{
   groupID:string,
}

export interface LockRecord_output{
}

   /** Required : 
      @param pcBankAcctID
      @param ds
   */  
export interface OnChangeBankAcctID_input{
      /**  Proposed bank account ID value.  */  
   pcBankAcctID:string,
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface OnChangeBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}
}

   /** Required : 
      @param ipBankExportFileName
      @param ds
   */  
export interface OnChangeBankExportFileName_input{
      /**  File name including the full path  */  
   ipBankExportFileName:string,
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface OnChangeBankExportFileName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}
}

   /** Required : 
      @param CheckDate
      @param ds
   */  
export interface OnChangeCheckDate_input{
      /**  Payment Date  */  
   CheckDate:string,
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface OnChangeCheckDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}
}

   /** Required : 
      @param piLoadedCheckNum
      @param ds
   */  
export interface OnChangeLoadedCheckNum_input{
      /**  Loaded check number  */  
   piLoadedCheckNum:number,
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface OnChangeLoadedCheckNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}
}

   /** Required : 
      @param inFileName
   */  
export interface OverwriteFileWarning_input{
   inFileName:string,
}

export interface OverwriteFileWarning_output{
parameters : {
      /**  output parameters  */  
   vWarningMessage:string,
}
}

   /** Required : 
      @param ds
      @param printRemit
   */  
export interface PreRunDirect_input{
   ds:Erp_Tablesets_ProcessPaymentTableset[],
      /**  This should be true if Forms to Generate is "Both" and we want to print Remit  */  
   printRemit:boolean,
}

export interface PreRunDirect_output{
}

   /** Required : 
      @param ds
   */  
export interface ReStartProcessPayment_input{
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface ReStartProcessPayment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}
}

   /** Required : 
      @param paramSetID
   */  
export interface RemoveDefaults_input{
      /**  The defaults are stored with a key of Company,UserID,ProgramID,ParamSetID and FieldName
            The values of all of these, except ParamSetID are controlled by the backend logic.
            In most cases the ParamSetID is blank. Usually for a single program the user can only have one set of defaults.
            This parameter provides multi parameters sets to be associated with a single report.
            As is the case of GL Financial Reports. The user picks from a list of reports to be run.
            In this case you would pass the GLFinancialParam.GLReportID as the ParamSetID  */  
   paramSetID:string,
}

export interface RemoveDefaults_output{
}

   /** Required : 
      @param ds
   */  
export interface RunDirect_input{
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface RunDirect_output{
}

   /** Required : 
      @param ds
   */  
export interface RunProcessPayment_input{
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface RunProcessPayment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface SaveDefaults_input{
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface SaveDefaults_output{
}

   /** Required : 
      @param maintProgram
      @param ds
   */  
export interface SaveProcessTask_input{
   maintProgram:string,
   ds:Erp_Tablesets_ProcessPaymentTableset[],
}

export interface SaveProcessTask_output{
}

   /** Required : 
      @param ds
      @param agentID
      @param agentSchedNum
      @param agentTaskNum
      @param maintProgram
   */  
export interface SubmitToAgent_input{
   ds:Erp_Tablesets_ProcessPaymentTableset[],
      /**  Agent ID that will run this task  */  
   agentID:string,
      /**  Identifies the agent schedule of when this task should be run.
           Set to zero if you want to run this immediately.  */  
   agentSchedNum:number,
      /**  Identifies the agent task number within the schedule that is to be updated.
           Set to zero if you want to create a new task.  */  
   agentTaskNum:number,
      /**  Identifies the Maintenance program to run  */  
   maintProgram:string,
}

export interface SubmitToAgent_output{
}

   /** Required : 
      @param eGroupID
   */  
export interface TestGroupProcessing_input{
      /**  Group ID  */  
   eGroupID:string,
}

export interface TestGroupProcessing_output{
parameters : {
      /**  output parameters  */  
   NegativeGroupList:string,
}
}

   /** Required : 
      @param ipGroupID
      @param ipCheckDate
   */  
export interface ValidateElecIntFile_input{
      /**  Group ID  */  
   ipGroupID:string,
      /**  Check Date  */  
   ipCheckDate:string,
}

export interface ValidateElecIntFile_output{
}

   /** Required : 
      @param inCurrencyCode
   */  
export interface getCurrencyID_input{
   inCurrencyCode:string,
}

export interface getCurrencyID_output{
   returnObj:string,
}

   /** Required : 
      @param inCompany
      @param inPMUID
      @param inUpdate
   */  
export interface getEFTProductionNumber_input{
   inCompany:string,
   inPMUID:number,
   inUpdate:boolean,
}

export interface getEFTProductionNumber_output{
   returnObj:number,
}

   /** Required : 
      @param CurBankAcctID
   */  
export interface getNextECheckNum_input{
   CurBankAcctID:string,
}

export interface getNextECheckNum_output{
   returnObj:number,
}

   /** Required : 
      @param pcBankAcctID
   */  
export interface getStartCheckNum_input{
   pcBankAcctID:string,
}

export interface getStartCheckNum_output{
   returnObj:number,
}

   /** Required : 
      @param iPO3PayType
      @param cGroupID
   */  
export interface paymentGroupingPO3_input{
      /**  PO3 Pay Type  */  
   iPO3PayType:number,
      /**  Group ID  */  
   cGroupID:string,
}

export interface paymentGroupingPO3_output{
parameters : {
      /**  output parameters  */  
   cErrorMsg:string,
}
}

   /** Required : 
      @param inCompany
      @param inGroupID
      @param inAllowZeroCheckAmt
      @param inValidateBySupplyer
      @param inSPecialPayType
   */  
export interface validateNegativePaymentExist_input{
   inCompany:string,
   inGroupID:string,
   inAllowZeroCheckAmt:boolean,
   inValidateBySupplyer:boolean,
   inSPecialPayType:number,
}

export interface validateNegativePaymentExist_output{
   returnObj:string,
}

   /** Required : 
      @param ttProcessPaymentParam
   */  
export interface validateProcessPaymentParam_input{
   ttProcessPaymentParam:Erp_Tablesets_ProcessPaymentParamRow[],
}

export interface validateProcessPaymentParam_output{
}

