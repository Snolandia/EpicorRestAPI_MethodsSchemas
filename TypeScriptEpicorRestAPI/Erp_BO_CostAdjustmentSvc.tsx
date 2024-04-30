import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CostAdjustmentSvc
// Description: Cost Adjustment Business Object
        Business object which provides the fields needed by
        the UI for the Coswt Adjustment process.
       
        Provides a dataset containing the fields necessary
        to build multiple PartTran records.
       
        Lewis Batcher
        10-14-2003
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/$metadata", {
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
   Summary: Invoke method GetCostAdjustment
   Description: Obtains the cost fields, part description, transaction date, cost method
and other fields for the Cost Adjustment UI.
   OperationID: GetCostAdjustment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCostAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCostAdjustment(requestBody:GetCostAdjustment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCostAdjustment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/GetCostAdjustment", {
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
         resolve(data as GetCostAdjustment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCostAdjustmentRow
   Description: Returns CostAdjustment with the cost fields, part description, transaction date, cost method
and other fields
   OperationID: GetCostAdjustmentRow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCostAdjustmentRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostAdjustmentRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCostAdjustmentRow(requestBody:GetCostAdjustmentRow_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCostAdjustmentRow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/GetCostAdjustmentRow", {
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
         resolve(data as GetCostAdjustmentRow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCostAdjustmentMultiple
   Description: It accepts a list of Partnumber and builds a CostAdjustmentDataSet.
The CostAdjustmentDataSet contains the cost fields, part description, transaction date, cost method
and other fields for the Cost Adjustment UI.
   OperationID: GetCostAdjustmentMultiple
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCostAdjustmentMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostAdjustmentMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCostAdjustmentMultiple(requestBody:GetCostAdjustmentMultiple_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCostAdjustmentMultiple_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/GetCostAdjustmentMultiple", {
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
         resolve(data as GetCostAdjustmentMultiple_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFIFOCosts
   Description: Obtains the FIFO costs for a part which has a cost method of 'F'.
   OperationID: GetFIFOCosts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFIFOCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFIFOCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFIFOCosts(requestBody:GetFIFOCosts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFIFOCosts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/GetFIFOCosts", {
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
         resolve(data as GetFIFOCosts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLotCosts
   Description: Obtains the lot costs for a part which has a cost method of 'T'.
   OperationID: GetLotCosts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLotCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLotCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLotCosts(requestBody:GetLotCosts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLotCosts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/GetLotCosts", {
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
         resolve(data as GetLotCosts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCostAdjustment
   Description: This method creates a new CostAdjustmentDataSet row entry.
   OperationID: GetNewCostAdjustment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCostAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCostAdjustment(requestBody:GetNewCostAdjustment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCostAdjustment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/GetNewCostAdjustment", {
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
         resolve(data as GetNewCostAdjustment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCostAdjustmentList
   Description: This method creates a new ttCostAdjustmentList row entry.
   OperationID: GetNewCostAdjustmentList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCostAdjustmentList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostAdjustmentList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCostAdjustmentList(requestBody:GetNewCostAdjustmentList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCostAdjustmentList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/GetNewCostAdjustmentList", {
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
         resolve(data as GetNewCostAdjustmentList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAvgMtlUnitCost
   Description: Call this method when the user changes the Average Material Unit Cost.
   OperationID: OnChangeAvgMtlUnitCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAvgMtlUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAvgMtlUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAvgMtlUnitCost(requestBody:OnChangeAvgMtlUnitCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAvgMtlUnitCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/OnChangeAvgMtlUnitCost", {
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
         resolve(data as OnChangeAvgMtlUnitCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFIFOMaterialCost
   Description: Call this method when the user changes the FIFO Material Unit Cost.
   OperationID: OnChangeFIFOMaterialCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFIFOMaterialCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFIFOMaterialCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFIFOMaterialCost(requestBody:OnChangeFIFOMaterialCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFIFOMaterialCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/OnChangeFIFOMaterialCost", {
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
         resolve(data as OnChangeFIFOMaterialCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLastMtlUnitCost
   Description: Call this method when the user changes the Last Material Unit Cost.
   OperationID: OnChangeLastMtlUnitCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLastMtlUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLastMtlUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLastMtlUnitCost(requestBody:OnChangeLastMtlUnitCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLastMtlUnitCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/OnChangeLastMtlUnitCost", {
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
         resolve(data as OnChangeLastMtlUnitCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: Call this method when the user enters a PartNum.
   OperationID: OnChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:OnChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/OnChangePartNum", {
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
         resolve(data as OnChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeStdMtlUnitCost
   Description: Call this method when the user changes the Standard Material Unit Cost.
   OperationID: OnChangeStdMtlUnitCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeStdMtlUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeStdMtlUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeStdMtlUnitCost(requestBody:OnChangeStdMtlUnitCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeStdMtlUnitCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/OnChangeStdMtlUnitCost", {
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
         resolve(data as OnChangeStdMtlUnitCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreSetCostAdjustment
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreSetCostAdjustment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreSetCostAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSetCostAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreSetCostAdjustment(requestBody:PreSetCostAdjustment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreSetCostAdjustment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/PreSetCostAdjustment", {
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
         resolve(data as PreSetCostAdjustment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetCostAdjustment
   Description: This procedure validates the fields in the CostAdjustment dataset.
Then updates the costs in the Part record, PartLot (if applicable)
and creates the appropriate PartTran records.
   OperationID: SetCostAdjustment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetCostAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCostAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetCostAdjustment(requestBody:SetCostAdjustment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetCostAdjustment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/SetCostAdjustment", {
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
         resolve(data as SetCostAdjustment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetCostAdjustmentForWeb
   Description: This procedure validates the fields in the CostAdjustment dataset.
Then updates the costs in the Part record, PartLot (if applicable)
and creates the appropriate PartTran records.
Specific for web (client) use.
   OperationID: SetCostAdjustmentForWeb
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetCostAdjustmentForWeb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCostAdjustmentForWeb_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetCostAdjustmentForWeb(requestBody:SetCostAdjustmentForWeb_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetCostAdjustmentForWeb_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/SetCostAdjustmentForWeb", {
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
         resolve(data as SetCostAdjustmentForWeb_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetCostAdjustmentCommon
   Description: This procedure validates the fields in the CostAdjustment dataset.
Then updates the costs in the Part record, PartLot (if applicable)
and creates the appropriate PartTran records.
If plant, warehouse, qty parameters are set then use them instead of current warehouse values
   OperationID: SetCostAdjustmentCommon
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetCostAdjustmentCommon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCostAdjustmentCommon_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetCostAdjustmentCommon(requestBody:SetCostAdjustmentCommon_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetCostAdjustmentCommon_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/SetCostAdjustmentCommon", {
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
         resolve(data as SetCostAdjustmentCommon_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailTranDocTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostAdjustmentSvc/GetAvailTranDocTypes", {
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
         resolve(data as GetAvailTranDocTypes_output)
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
export interface Erp_Tablesets_CostAdjustmentListRow{
      /**  Company Identifier  */  
   Company:string,
   PartNum:string,
   SearchWord:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostAdjustmentListTableset{
   CostAdjustmentList:Erp_Tablesets_CostAdjustmentListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CostAdjustmentRow{
      /**  Company  */  
   Company:string,
      /**  Part Number.  */  
   PartNum:string,
      /**  Part description  */  
   PartDescription:string,
      /**  Cost Method  */  
   CostMethod:string,
      /**  Transaction date  */  
   TransDate:string,
      /**  Lot number  */  
   LotNum:string,
      /**  Reason code  */  
   ReasonCode:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  Reference  */  
   Reference:string,
      /**  Average material unit cost  */  
   AvgMtlUnitCost:number,
      /**  Average labor unit cost  */  
   AvgLbrUnitCost:number,
      /**  Average burden unit cost  */  
   AvgBurUnitCost:number,
      /**  Average subcontract unit cost  */  
   AvgSubUnitCost:number,
      /**  Average material burden unit cost  */  
   AvgMatBurUnitCost:number,
      /**  Average total unit cost  */  
   AvgTotUnitCost:number,
      /**  Last material unit cost  */  
   LastMtlUnitCost:number,
      /**  Last labor unit cost  */  
   LastLbrUnitCost:number,
      /**  Last burden unit cost  */  
   LastBurUnitCost:number,
      /**  Last subcontract unit cost  */  
   LastSubUnitCost:number,
      /**  Last material burden unit cost  */  
   LastMatBurUnitCost:number,
      /**  Last total unit cost  */  
   LastTotUnitCost:number,
      /**  Standard material unit cost  */  
   StdMtlUnitCost:number,
      /**  Standard labor unit cost  */  
   StdLbrUnitCost:number,
      /**  Standard burden unit cost  */  
   StdBurUnitCost:number,
      /**  Standard subcontract unit cost  */  
   StdSubUnitCost:number,
      /**  Standard material burden unit cost  */  
   StdMatBurUnitCost:number,
      /**  Standard total unit cost  */  
   StdTotUnitCost:number,
      /**  Original average material unit cost  */  
   OrigAvgMtlUnitCost:number,
      /**  Original average labor unit cost  */  
   OrigAvgLbrUnitCost:number,
      /**  Original average subcontract unit cost  */  
   OrigAvgSubUnitCost:number,
      /**  Original average material burden unit cost  */  
   OrigAvgMatBurUnitCost:number,
      /**  Original last material unit cost  */  
   OrigLastMtlUnitCost:number,
      /**  Original last labor unit cost  */  
   OrigLastLbrUnitCost:number,
      /**  Original last burden unit cost  */  
   OrigLastBurUnitCost:number,
      /**  Original last subcontract unit cost  */  
   OrigLastSubUnitCost:number,
      /**  Original last material burden unit cost  */  
   OrigLastMatBurUnitCost:number,
      /**  Original average burden unit cost  */  
   OrigAvgBurUnitCost:number,
      /**  Original standard material unit cost  */  
   OrigStdMtlUnitCost:number,
      /**  Original standard labor unit cost  */  
   OrigStdLbrUnitCost:number,
      /**  Original standard burden unit cost  */  
   OrigStdBurUnitCost:number,
      /**  Original standard subcontract unit cost  */  
   OrigStdSubUnitCost:number,
      /**  Original standard material burden unit cost  */  
   OrigStdMatBurUnitCost:number,
      /**  Cost method description  */  
   CostMethodDisplay:string,
   TransactionPosted:boolean,
      /**  Dummy field to make the records unique.  Required for providing multiple cost adjustment capabality for a part.  */  
   DummyKeyField:number,
   LegalNumberMessage:string,
   TrackLots:boolean,
      /**  FIFO Unit Burden Cost  */  
   FIFOBurdenCost:number,
      /**  This could be the transaction date or the system date at the time this FIFO cost record was created.  Depending on the setting at Company Configuration (XbSyst.UseTranDate).  */  
   FIFODate:string,
      /**  FIFO Unit Labor Cost  */  
   FIFOLaborCost:number,
      /**  FIFO Unit Material Cost  */  
   FIFOMaterialCost:number,
      /**  FIFO Unit Material Burden Cost  */  
   FIFOMtlBurCost:number,
      /**  A number which is used to allow create a unique key for the file.  */  
   FIFOSeq:number,
      /**  FIFO Unit Subcontract Cost  */  
   FIFOSubContCost:number,
      /**  FIFO Total Cost. FIFOBurdenCost + FIFOLaborCost + FIFOMaterialCost + FIFOMtlBurCost + FIFOSubContCost  */  
   FIFOTotalCost:number,
   CostID:string,
      /**  Original FIFO burden unit cost  */  
   OrigFIFOBurdenCost:number,
      /**  Original FIFO labor unit cost  */  
   OrigFIFOLaborCost:number,
      /**  Original FIFO material unit cost  */  
   OrigFIFOMaterialCost:number,
      /**  Original FIFO material burden unit cost  */  
   OrigFIFOMtlBurCost:number,
      /**  Original FIFO subcontract unit cost  */  
   OrigFIFOSubContCost:number,
      /**  Indicates if valid FIFO is found.  */  
   EnableFIFOCosts:boolean,
      /**  Indicates if valid PartLot is found.  */  
   EnableLotCosts:boolean,
      /**  FIFO Subsequence  */  
   FIFOSubSeq:number,
      /**  Indicates if the logic for the FIFO Layers is enabled.  */  
   EnableFIFOLayers:boolean,
      /**  FIFO Average Burden Unit Cost  */  
   FIFOAvgBurUnitCost:number,
      /**  FIFO Average Labor Unit Cost  */  
   FIFOAvgLbrUnitCost:number,
      /**  FIFO Average Material Unit Cost  */  
   FIFOAvgMtlUnitCost:number,
      /**  FIFO Average Subcontract Unit Cost  */  
   FIFOAvgSubUnitCost:number,
      /**  FIFO Average Material Burden Unit Cost  */  
   FIFOAvgMatBurUnitCost:number,
      /**  FIFO Average Total Unit Cost  */  
   FIFOAvgTotUnitCost:number,
      /**  Original FIFO Average Burden Unit Cost  */  
   OrigFIFOAvgBurUnitCost:number,
      /**  Original FIFO Average Labor Unit Cost  */  
   OrigFIFOAvgLbrUnitCost:number,
      /**  Original FIFO Average Material UInit Cost  */  
   OrigFIFOAvgMtlUnitCost:number,
      /**  Original FIFO Average Subcontract Unit Cost  */  
   OrigFIFOAvgSubUnitCost:number,
      /**  Original FIFO Average Material Burden Unit Cost  */  
   OrigFIFOAvgMatBurUnitCost:number,
   TranDocTypeID:string,
      /**  Legal Number assigned  */  
   LegalNumber:string,
      /**  VarTarget, used for PartTran creating in Actual Cost Allocation Post process (value ACA - Actual Cost Allocation)  */  
   VarTarget:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostAdjustmentTableset{
   CostAdjustment:Erp_Tablesets_CostAdjustmentRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   listAvailTranDocTypes:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetCostAdjustmentMultiple_input{
   ds:Erp_Tablesets_CostAdjustmentListTableset[],
}

export interface GetCostAdjustmentMultiple_output{
   returnObj:Erp_Tablesets_CostAdjustmentTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentListTableset,
}
}

   /** Required : 
      @param pcPartNumber
      @param applyDate
   */  
export interface GetCostAdjustmentRow_input{
      /**  The part number entered by the user..  */  
   pcPartNumber:string,
      /**  Cost Adjustment Apply/Transaction Date  */  
   applyDate:string,
}

export interface GetCostAdjustmentRow_output{
   returnObj:Erp_Tablesets_CostAdjustmentRow[],
parameters : {
      /**  output parameters  */  
   hasError:boolean,
}
}

   /** Required : 
      @param pcPartNumber
      @param ds
   */  
export interface GetCostAdjustment_input{
      /**  The part number entered by the user..  */  
   pcPartNumber:string,
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface GetCostAdjustment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetFIFOCosts_input{
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface GetFIFOCosts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetLotCosts_input{
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface GetLotCosts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCostAdjustmentList_input{
   ds:Erp_Tablesets_CostAdjustmentListTableset[],
}

export interface GetNewCostAdjustmentList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentListTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCostAdjustment_input{
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface GetNewCostAdjustment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
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
      @param dAvgMtlUnitCost
      @param ds
   */  
export interface OnChangeAvgMtlUnitCost_input{
      /**  The average material unit cost entered by the user..  */  
   dAvgMtlUnitCost:number,
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface OnChangeAvgMtlUnitCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
}
}

   /** Required : 
      @param dFIFOMaterialCost
      @param ds
   */  
export interface OnChangeFIFOMaterialCost_input{
      /**  The FIFO material unit cost entered by the user.  */  
   dFIFOMaterialCost:number,
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface OnChangeFIFOMaterialCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
}
}

   /** Required : 
      @param dLastMtlUnitCost
      @param ds
   */  
export interface OnChangeLastMtlUnitCost_input{
      /**  The last material unit cost entered by the user..  */  
   dLastMtlUnitCost:number,
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface OnChangeLastMtlUnitCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
}
}

   /** Required : 
      @param pcPartNumber
      @param ds
   */  
export interface OnChangePartNum_input{
      /**  The part number entered by the user..  */  
   pcPartNumber:string,
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
}
}

   /** Required : 
      @param dStdMtlUnitCost
      @param ds
   */  
export interface OnChangeStdMtlUnitCost_input{
      /**  The standard material unit cost entered by the user..  */  
   dStdMtlUnitCost:number,
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface OnChangeStdMtlUnitCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface PreSetCostAdjustment_input{
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface PreSetCostAdjustment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
      @param allowEmptyReason
      @param ipPlant
      @param ipWarehouseCode
      @param ipOnHandQty
   */  
export interface SetCostAdjustmentCommon_input{
   ds:Erp_Tablesets_CostAdjustmentTableset[],
      /**  Allow Empty Reason for Cost Adjustment  */  
   allowEmptyReason:boolean,
      /**  plant  */  
   ipPlant:string,
      /**  warehouse  */  
   ipWarehouseCode:string,
      /**  quantity  */  
   ipOnHandQty:number,
}

export interface SetCostAdjustmentCommon_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
   partTranPKs:string,
   hasError:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface SetCostAdjustmentForWeb_input{
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface SetCostAdjustmentForWeb_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
   partTranPKs:string,
}
}

   /** Required : 
      @param ds
   */  
export interface SetCostAdjustment_input{
   ds:Erp_Tablesets_CostAdjustmentTableset[],
}

export interface SetCostAdjustment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostAdjustmentTableset,
   partTranPKs:string,
}
}

