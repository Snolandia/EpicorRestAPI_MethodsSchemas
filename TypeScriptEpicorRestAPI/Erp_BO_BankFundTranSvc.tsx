import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.BankFundTranSvc
// Description: bo/BankFundTran/BankFundTran.p
           Bank Funds Transfer
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method ChangeFromAmt
   Description: This method validates the proposed Tranfer Amount and updates the dataset accordingly
   OperationID: ChangeFromAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFromAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFromAmt(requestBody:ChangeFromAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFromAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/ChangeFromAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeFromAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFromBank
   Description: This method validates the proposed from (source) bank and updates the dataset accordingly
   OperationID: ChangeFromBank
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFromBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFromBank(requestBody:ChangeFromBank_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFromBank_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/ChangeFromBank", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeFromBank_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRateGrp
   Description: This method validates the proposed RateGrpCode and updates the dataset accordingly
   OperationID: ChangeRateGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRateGrp(requestBody:ChangeRateGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRateGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/ChangeRateGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRateGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTargetBank
   Description: This method validates the proposed target bank and updates the dataset accordingly
   OperationID: ChangeTargetBank
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTargetBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTargetBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTargetBank(requestBody:ChangeTargetBank_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTargetBank_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/ChangeTargetBank", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTargetBank_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeToAmt
   Description: This method validates the proposed To Tranfer Amount and updates the dataset accordingly
   OperationID: ChangeToAmt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeToAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeToAmt(requestBody:ChangeToAmt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeToAmt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/ChangeToAmt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeToAmt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTranDate
   Description: This method validates the proposed Transaction date and updates the dataset according
to the new date/fiscal period
   OperationID: ChangeTranDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTranDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTranDate(requestBody:ChangeTranDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTranDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/ChangeTranDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeTranDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateBankTran
   Description: This method creates the BankFundTran record for the user to edit
   OperationID: CreateBankTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateBankTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateBankTran(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateBankTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/CreateBankTran", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateBankTran_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateBankTranRecords
   Description: This method creates 2 BankTran records before posting them
   OperationID: CreateBankTranRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateBankTranRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateBankTranRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateBankTranRecords(requestBody:CreateBankTranRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateBankTranRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/CreateBankTranRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateBankTranRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLegalNumGenOpts
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: GetLegalNumGenOpts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegalNumGenOpts(requestBody:GetLegalNumGenOpts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLegalNumGenOpts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/GetLegalNumGenOpts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetLegalNumGenOpts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateBeforeTransfer
   Description: This method validates all entered data, that need to do before transfer.
   OperationID: ValidateBeforeTransfer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateBeforeTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBeforeTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBeforeTransfer(requestBody:ValidateBeforeTransfer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateBeforeTransfer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/ValidateBeforeTransfer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateBeforeTransfer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByTranNum
   Description: Returns dataset filled with data found by TranNum
   OperationID: GetByTranNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByTranNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByTranNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByTranNum(requestBody:GetByTranNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByTranNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/GetByTranNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByTranNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateBankTranRecords
   Description: This method upadtes 2 BankTran records and save them. Works only with unposted records.
   OperationID: UpdateBankTranRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateBankTranRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateBankTranRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateBankTranRecords(requestBody:UpdateBankTranRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateBankTranRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/UpdateBankTranRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateBankTranRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PESelectDetractionInvoices
   Description: This procedure returns invoices with Detractions to be paid
   OperationID: PESelectDetractionInvoices
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PESelectDetractionInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PESelectDetractionInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PESelectDetractionInvoices(requestBody:PESelectDetractionInvoices_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PESelectDetractionInvoices_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/PESelectDetractionInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PESelectDetractionInvoices_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PEUpdateInvcHeadRecords
   Description: This procedure updates selected InvcHead
   OperationID: PEUpdateInvcHeadRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PEUpdateInvcHeadRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PEUpdateInvcHeadRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PEUpdateInvcHeadRecords(requestBody:PEUpdateInvcHeadRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PEUpdateInvcHeadRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BankFundTranSvc/PEUpdateInvcHeadRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PEUpdateInvcHeadRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param docTranAmt
      @param ds
      @param isFirstBank
   */  
export interface ChangeFromAmt_input{
      /**  Proposed Transaction Amount  */  
   docTranAmt:number,
   ds:Erp_Tablesets_BankFundTranTableset[],
      /**  Indicates whether the source bank is the first bank selected  */  
   isFirstBank:boolean,
}

export interface ChangeFromAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFundTranTableset,
}
}

   /** Required : 
      @param bankAcctID
      @param ds
      @param isFirstBank
   */  
export interface ChangeFromBank_input{
      /**  Proposed From Bank Accout ID  */  
   bankAcctID:string,
   ds:Erp_Tablesets_BankFundTranTableset[],
      /**  Indicates whether the source bank is the first bank selected  */  
   isFirstBank:boolean,
}

export interface ChangeFromBank_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFundTranTableset,
}
}

   /** Required : 
      @param ipRateGrpCode
      @param ds
   */  
export interface ChangeRateGrp_input{
      /**  Proposed RateGrpCode  */  
   ipRateGrpCode:string,
   ds:Erp_Tablesets_BankFundTranTableset[],
}

export interface ChangeRateGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFundTranTableset,
}
}

   /** Required : 
      @param toBankAcctID
      @param ds
      @param isFirstBank
   */  
export interface ChangeTargetBank_input{
      /**  Proposed Target Bank Accout ID  */  
   toBankAcctID:string,
   ds:Erp_Tablesets_BankFundTranTableset[],
      /**  Indicates whether the target bank is the first bank selected  */  
   isFirstBank:boolean,
}

export interface ChangeTargetBank_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFundTranTableset,
}
}

   /** Required : 
      @param toDocTranAmt
      @param ds
      @param isFirstBank
   */  
export interface ChangeToAmt_input{
      /**  Proposed To Transaction Amount  */  
   toDocTranAmt:number,
   ds:Erp_Tablesets_BankFundTranTableset[],
      /**  Indicates whether the target bank is the first bank selected  */  
   isFirstBank:boolean,
}

export interface ChangeToAmt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFundTranTableset,
}
}

   /** Required : 
      @param tranDate
      @param ds
      @param fromSourceBank
   */  
export interface ChangeTranDate_input{
      /**  Proposed Transaction Date  */  
   tranDate:string,
   ds:Erp_Tablesets_BankFundTranTableset[],
      /**  Shows that transfer creation began from source bank (true, default) or target bank (false)  */  
   fromSourceBank:boolean,
}

export interface ChangeTranDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFundTranTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CreateBankTranRecords_input{
   ds:Erp_Tablesets_BankFundTranTableset[],
}

export interface CreateBankTranRecords_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFundTranTableset,
}
}

export interface CreateBankTran_output{
   returnObj:Erp_Tablesets_BankFundTranTableset[],
}

export interface Erp_Tablesets_BankFundTranTableset{
   BankFundsTransfer:Erp_Tablesets_BankFundsTransferRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_BankFundsTransferRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Relates record to a BankAcct.  */  
   BankAcctID:string,
      /**  Unique ID of the Transaction.  */  
   TranNum:number,
      /**  Date that the transaction took place.  */  
   TranDate:string,
      /**  Amount of the Transaction  */  
   TranAmt:number,
      /**  Transaction Reference  */  
   TranRef:string,
      /**  Indicates that the Transaction (not cleared variance) has been posted to G/L.  When the Bank Statement is posted all Non-G/L Posted adjustments for the bank are posted to G/L using the Bank Account's Cash and Bank Fee Accounts. G/L Posted Transactions cannot be deleted. (System Set)  */  
   GLPosted:boolean,
      /**  Person who entered the transaction (System Set).  */  
   EntryPerson:string,
      /**  Date that the Transaction was entered into the system (System Set).  */  
   EntryDate:string,
      /**  Time that the transaction was entered into the system - in HH:MM:SS format (System Set).  */  
   EntryTime:string,
      /**  Indicates the transaction's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   TranCleared:boolean,
      /**  Indicates that the transaction is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   TranClearPending:boolean,
      /**  Amount that the Transaction was cleared for.  */  
   TranClearedAmt:number,
      /**  Person who cleared the transaction (System Set).  */  
   TranClearedPerson:string,
      /**  Date that the Transaction was cleared in the system (System Set).  */  
   TranClearedDate:string,
      /**  Time that the transaction was cleared in the system - in HH:MM:SS format (System Set).  */  
   TranClearedTime:string,
      /**  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  */  
   BankSlip:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Fiscal period the transaction was posted to. Only pertains to when posted to GL.  */  
   FiscalPeriod:number,
      /**  Journal Number of related GLJrnDtl.  */  
   JournalNum:number,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Document amount of the Transaction  */  
   DocTranAmt:number,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Exchange rate that is used for this bank transaction.  */  
   ExchangeRate:number,
      /**  Document amount that the Transaction was cleared for.  */  
   DocTranClearedAmt:number,
      /**  The data entry "group" that the transaction is assigned to.  All transactions belong to a "Group."  It is assigned to the record during creation using the "current group" that the user is signed into.  It cannot be changed.  The GroupID is used to selectively print and post the transactions.  */  
   GroupID:string,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  */  
   GLRefCodeDesc:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal year suffix that entry applies to.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Indiates if the BankTran has been voided.  The TranNum field will be the same as the original transaction  */  
   Voided:boolean,
      /**  Legal Number for the record.  */  
   LegalNumber:string,
      /**  Transaction Document for the record.  */  
   TranDocTypeID:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CNCFICode  */  
   CNCFICode:string,
      /**  CNToCFICode  */  
   CNToCFICode:string,
      /**  Multi-Site related Site  */  
   Plant:string,
   RefDisplayAccount:string,
      /**  Transfer To BankAccount ID  */  
   ToBankAcctID:string,
      /**  Transfer To Bank Account Description  */  
   ToBankDesc:string,
   FromBalance:number,
   FromNewBalance:number,
   ToBalance:number,
   ToNewBalance:number,
   FromCurrSymbol:string,
   ToCurrSymbol:string,
   ToExchangeRate:number,
   ToTranAmt:number,
   ToDocTranAmt:number,
   ToCurrencyCode:string,
   Rpt1ToTranAmt:number,
   Rpt2ToTranAmt:number,
   Rpt3ToTranAmt:number,
      /**  shows is this invoice is blocked in RvLock  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process  */  
   LockStatus:string,
   LegalNumMessage:string,
      /**  Indicates if the legal number is manually generated or system generated  */  
   LegalNumStyle:string,
   CNCFICodeDescription:string,
   CNToCFICodeDescription:string,
      /**  Peru CSF - Detractions candidates amount  */  
   PECandidatesAmt:number,
      /**  Peru CSF - Detractions remaining amount  */  
   PERemainingAmt:number,
      /**  Peru CSF - Detractions selected amount  */  
   PESelectedAmt:number,
      /**  Peru CSF - Detraction Exchange Rate  */  
   PEExchangeRate:number,
   ToPlant:string,
   BitFlag:number,
   BankAcctDescription:string,
   BankAcctBankName:string,
   BankAcctToPEDetNationalBank:boolean,
   BankAcctToDescription:string,
   BankAcctToCurrencyCode:string,
   RateGrpDescription:string,
   XbSystSiteIsLegalEntity:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PEARInvSelRow{
   Selected:boolean,
   InvoiceNum:number,
   LegalNumber:string,
   CustNum:number,
   Name:string,
   ApplyDate:string,
   DetractionTaxAmt:number,
   LastCashReceiptDate:string,
   ProductCode:string,
   CustID:string,
   CurrencyCode:string,
   DocDetractionTaxAmt:number,
   DueDate:string,
   InvoiceDate:string,
   CustBalance:number,
   CustAmount:number,
   Balance:number,
   InvoiceAmt:number,
   PECollectionsDate:string,
   InvInCollections:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PEARInvSelTableset{
   PEARInvSel:Erp_Tablesets_PEARInvSelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param TranNum
   */  
export interface GetByTranNum_input{
      /**  TarnNum  */  
   TranNum:number,
}

export interface GetByTranNum_output{
   returnObj:Erp_Tablesets_BankFundTranTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetLegalNumGenOpts_input{
   ds:Erp_Tablesets_BankFundTranTableset[],
}

export interface GetLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFundTranTableset,
   RequiresUserInput:boolean,
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
      @param dsBankFundTran
      @param dsPEARInvSel
   */  
export interface PESelectDetractionInvoices_input{
   dsBankFundTran:Erp_Tablesets_BankFundTranTableset[],
   dsPEARInvSel:Erp_Tablesets_PEARInvSelTableset[],
}

export interface PESelectDetractionInvoices_output{
parameters : {
      /**  output parameters  */  
   dsBankFundTran:Erp_Tablesets_BankFundTranTableset,
   dsPEARInvSel:Erp_Tablesets_PEARInvSelTableset,
}
}

   /** Required : 
      @param dsBankFundTran
      @param dsPEARInvSel
   */  
export interface PEUpdateInvcHeadRecords_input{
   dsBankFundTran:Erp_Tablesets_BankFundTranTableset[],
   dsPEARInvSel:Erp_Tablesets_PEARInvSelTableset[],
}

export interface PEUpdateInvcHeadRecords_output{
parameters : {
      /**  output parameters  */  
   dsBankFundTran:Erp_Tablesets_BankFundTranTableset,
   dsPEARInvSel:Erp_Tablesets_PEARInvSelTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateBankTranRecords_input{
   ds:Erp_Tablesets_BankFundTranTableset[],
}

export interface UpdateBankTranRecords_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFundTranTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateBeforeTransfer_input{
   ds:Erp_Tablesets_BankFundTranTableset[],
}

export interface ValidateBeforeTransfer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BankFundTranTableset,
}
}

