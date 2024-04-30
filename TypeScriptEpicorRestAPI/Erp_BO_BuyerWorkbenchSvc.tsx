import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.BuyerWorkbenchSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/$metadata", {
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
   Summary: Invoke method AddSuggSupplier
   Description: This methods will add supplier record for an individual suggestion.
   OperationID: AddSuggSupplier
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddSuggSupplier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddSuggSupplier_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddSuggSupplier(requestBody:AddSuggSupplier_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddSuggSupplier_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/AddSuggSupplier", {
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
         resolve(data as AddSuggSupplier_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRFQSuggVendPurPoint
   Description: This method validates the RFQSuggVend.PurPoint when it changes.
This method should run when changing the RFQSuggVend.PurPoint.
   OperationID: ChangeRFQSuggVendPurPoint
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRFQSuggVendPurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRFQSuggVendPurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRFQSuggVendPurPoint(requestBody:ChangeRFQSuggVendPurPoint_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRFQSuggVendPurPoint_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/ChangeRFQSuggVendPurPoint", {
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
         resolve(data as ChangeRFQSuggVendPurPoint_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRFQSuggVendVendorID
   Description: This methods takes the RFQSuggVend.VendorNum and populates the associated fields
with value based on the vendornum.
This method should run when changing the RFQSuggVend.VendorNum.
   OperationID: ChangeRFQSuggVendVendorID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRFQSuggVendVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRFQSuggVendVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRFQSuggVendVendorID(requestBody:ChangeRFQSuggVendVendorID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRFQSuggVendVendorID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/ChangeRFQSuggVendVendorID", {
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
         resolve(data as ChangeRFQSuggVendVendorID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRFQSuggVendVendorID
   Description: This methods checks to see if the new RFQSuggVend.VendorNum has changed from the original
RFQSuggVend.VendorNum and validates the value.
This method should run before changing the RFQSuggVend.VendorNum.
   OperationID: CheckRFQSuggVendVendorID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRFQSuggVendVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRFQSuggVendVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRFQSuggVendVendorID(requestBody:CheckRFQSuggVendVendorID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRFQSuggVendVendorID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/CheckRFQSuggVendVendorID", {
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
         resolve(data as CheckRFQSuggVendVendorID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateDatasetWithCounters
   Description: This methods will return all of the records for the Buyer Workbench.
   OperationID: CreateDatasetWithCounters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateDatasetWithCounters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDatasetWithCounters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateDatasetWithCounters(requestBody:CreateDatasetWithCounters_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateDatasetWithCounters_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/CreateDatasetWithCounters", {
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
         resolve(data as CreateDatasetWithCounters_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateDataset
   Description: This methods will return all of the records for the Buyer Workbench.
   OperationID: CreateDataset
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateDataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateDataset(requestBody:CreateDataset_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateDataset_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/CreateDataset", {
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
         resolve(data as CreateDataset_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteSuggSupplier
   Description: This methods will delete supplier record for an individual suggestion.
   OperationID: DeleteSuggSupplier
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteSuggSupplier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSuggSupplier_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteSuggSupplier(requestBody:DeleteSuggSupplier_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteSuggSupplier_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/DeleteSuggSupplier", {
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
         resolve(data as DeleteSuggSupplier_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeselectAll
   Description: This method will change the ProcessRFQ field in the RFQSugg table and the
RFQSuggBWB temp table to false (deselected) for the inputted buyerid.
   OperationID: DeselectAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeselectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeselectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeselectAll(requestBody:DeselectAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeselectAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/DeselectAll", {
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
         resolve(data as DeselectAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Generate
   Description: This method will generate RFQ's for lines.  This method can generate for all
suggestions for a buyer by only entering a buyerid or a specific suggestion by
also entering a suggestion number.  This method will call CreateDataset at the
end of running to refresh the dataset.
   OperationID: Generate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Generate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Generate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Generate(requestBody:Generate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Generate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/Generate", {
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
         resolve(data as Generate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSugPOChgCount
   Description: This methods will return a count of Change PO Suggestions for the selected Buyer
   OperationID: GetSugPOChgCount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSugPOChgCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSugPOChgCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSugPOChgCount(requestBody:GetSugPOChgCount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSugPOChgCount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/GetSugPOChgCount", {
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
         resolve(data as GetSugPOChgCount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSugPoDtlCount
   Description: This methods will return a count of NEW PO Suggestions for the selected Buyer
   OperationID: GetSugPoDtlCount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSugPoDtlCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSugPoDtlCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSugPoDtlCount(requestBody:GetSugPoDtlCount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSugPoDtlCount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/GetSugPoDtlCount", {
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
         resolve(data as GetSugPoDtlCount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSuggSupp
   Description: This methods will create a blank RFQSuggVend record for an individual suggestion
and allow the user to type in field values through the grid.
   OperationID: GetNewSuggSupp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSuggSupp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSuggSupp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSuggSupp(requestBody:GetNewSuggSupp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSuggSupp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/GetNewSuggSupp", {
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
         resolve(data as GetNewSuggSupp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectAll
   Description: This method will change the ProcessRFQ field in the RFQSugg table and the
RFQSuggBWB temp table to true (selected) for the inputted buyerid.
   OperationID: SelectAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectAll(requestBody:SelectAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/SelectAll", {
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
         resolve(data as SelectAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SupplierWizard
   Description: This methods will return suppliers for the suggestion
   OperationID: SupplierWizard
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SupplierWizard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SupplierWizard_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SupplierWizard(requestBody:SupplierWizard_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SupplierWizard_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BuyerWorkbenchSvc/SupplierWizard", {
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
         resolve(data as SupplierWizard_output)
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
      @param ipBuyerID
      @param ipSugNum
      @param ipVendorNum
      @param ipPurPoint
      @param ds
   */  
export interface AddSuggSupplier_input{
      /**  The buyer id to add data for.  */  
   ipBuyerID:string,
      /**  The suggestion number to link suppliers to.  */  
   ipSugNum:number,
      /**  The vendor number of the supplier to add.  */  
   ipVendorNum:number,
      /**  The purchase point of the supplier to add.  */  
   ipPurPoint:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset[],
}

export interface AddSuggSupplier_output{
parameters : {
      /**  output parameters  */  
   opStatusMsg:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset,
}
}

   /** Required : 
      @param ipRFQSuggVendRowid
      @param ds
   */  
export interface ChangeRFQSuggVendPurPoint_input{
      /**  The rowident of the record being updated/created.  */  
   ipRFQSuggVendRowid:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset[],
}

export interface ChangeRFQSuggVendPurPoint_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BuyerWorkbenchTableset,
}
}

   /** Required : 
      @param ipBuyerID
      @param ipRFQSuggVendRowid
      @param ds
   */  
export interface ChangeRFQSuggVendVendorID_input{
      /**  The buyer id used to locate records.  */  
   ipBuyerID:string,
      /**  The rowident of the record being updated/created.  */  
   ipRFQSuggVendRowid:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset[],
}

export interface ChangeRFQSuggVendVendorID_output{
parameters : {
      /**  output parameters  */  
   opStatusMsg:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset,
}
}

   /** Required : 
      @param ipProposedVendorID
      @param ipRFQSuggVendRowid
      @param ds
   */  
export interface CheckRFQSuggVendVendorID_input{
      /**  The new proposed RFQSuggVend.VendorID value  */  
   ipProposedVendorID:string,
      /**  The rowident of the record being updated/created.  */  
   ipRFQSuggVendRowid:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset[],
}

export interface CheckRFQSuggVendVendorID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BuyerWorkbenchTableset,
}
}

   /** Required : 
      @param ipBuyerID
   */  
export interface CreateDatasetWithCounters_input{
      /**  The buyer id to return data for.  */  
   ipBuyerID:string,
}

export interface CreateDatasetWithCounters_output{
   returnObj:Erp_Tablesets_BuyerWorkbenchTableset[],
parameters : {
      /**  output parameters  */  
   poSuggCount:number,
   poSuggChgCount:number,
}
}

   /** Required : 
      @param ipBuyerID
   */  
export interface CreateDataset_input{
      /**  The buyer id to return data for.  */  
   ipBuyerID:string,
}

export interface CreateDataset_output{
   returnObj:Erp_Tablesets_BuyerWorkbenchTableset[],
}

   /** Required : 
      @param ipSugNum
      @param ipVendorNum
      @param ds
   */  
export interface DeleteSuggSupplier_input{
      /**  The suggestion number to delete suppliers for.  */  
   ipSugNum:number,
      /**  The vendor number of the supplier to delete.  */  
   ipVendorNum:number,
   ds:Erp_Tablesets_BuyerWorkbenchTableset[],
}

export interface DeleteSuggSupplier_output{
parameters : {
      /**  output parameters  */  
   opStatusMsg:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset,
}
}

   /** Required : 
      @param ipBuyerID
      @param ds
   */  
export interface DeselectAll_input{
      /**  The buyer id to deselect all for.  */  
   ipBuyerID:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset[],
}

export interface DeselectAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BuyerWorkbenchTableset,
}
}

export interface Erp_Tablesets_BuyerWorkbenchTableset{
   POTotal:Erp_Tablesets_POTotalRow[],
   POApproval:Erp_Tablesets_POApprovalRow[],
   POChangeSugg:Erp_Tablesets_POChangeSuggRow[],
   POFuture:Erp_Tablesets_POFutureRow[],
   POLate:Erp_Tablesets_POLateRow[],
   PONewSugg:Erp_Tablesets_PONewSuggRow[],
   POReject:Erp_Tablesets_PORejectRow[],
   POThisWeek:Erp_Tablesets_POThisWeekRow[],
   POToday:Erp_Tablesets_POTodayRow[],
   RFQTotal:Erp_Tablesets_RFQTotalRow[],
   RFQFuture:Erp_Tablesets_RFQFutureRow[],
   RFQOverdue:Erp_Tablesets_RFQOverdueRow[],
   RFQReady:Erp_Tablesets_RFQReadyRow[],
   RFQSuggBWB:Erp_Tablesets_RFQSuggBWBRow[],
   RFQSuggVend:Erp_Tablesets_RFQSuggVendRow[],
   RFQThisWeek:Erp_Tablesets_RFQThisWeekRow[],
   RFQToday:Erp_Tablesets_RFQTodayRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_POApprovalRow{
      /**  The company identifier  */  
   Company:string,
      /**  The po number.  */  
   PONum:number,
      /**  The message type.  */  
   MsgType:string,
      /**  The message date.  */  
   MsgDate:string,
      /**  The message time.  */  
   MsgTime:number,
      /**  The message to value.  */  
   MsgTo:string,
      /**  The message from value.  */  
   MsgFrom:string,
      /**  The approver's response.  */  
   ApproverResponse:string,
      /**  The user id.  */  
   DCDUserID:string,
      /**  The buyer id.  */  
   BuyerID:string,
      /**  Text for communication.  */  
   MsgText:string,
      /**  The buyer id name.  */  
   BuyerName:string,
      /**  The buyer name of the buyerid in the msgto field.  */  
   MsgToName:string,
      /**  The buyer name for the buyerid in the msgfrom field.  */  
   MsgFromName:string,
      /**  The formatted representation of the msgtime field.  */  
   FormattedMsgTime:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POChangeSuggRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The po number.  */  
   PONum:number,
      /**  The po release line number.  */  
   POLine:number,
      /**  The po release number.  */  
   PORelNum:number,
      /**  The buyer id.  */  
   BuyerID:string,
      /**  The require date.  */  
   RequireDate:string,
      /**  The plant identifier.  */  
   Plant:string,
      /**  The part number.  */  
   PartNum:string,
      /**  The description of the part number.  */  
   PartDescription:string,
      /**  The suggestion text or exception text  */  
   Suggestion:string,
      /**  The vendor id.  */  
   VendorID:string,
      /**  The vendor name.  */  
   VendName:string,
      /**  The purchase point.  */  
   PurPoint:string,
      /**  The vendor change flag.  */  
   VendorChange:boolean,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POFutureRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The po number.  */  
   PONum:number,
      /**  The po line number.  */  
   POLine:number,
      /**  The po release number.  */  
   PORelNum:number,
      /**  The due date.  */  
   DueDate:string,
      /**  The promise date.  */  
   PromiseDt:string,
      /**  The job number.  */  
   JobNum:string,
      /**  The part number.  */  
   PartNum:string,
      /**  The description of the part number.  */  
   PartDescription:string,
      /**  The release quantity.  */  
   RelQty:number,
      /**  The received quantity.  */  
   ReceivedQty:number,
      /**  The remaining quantity.  */  
   RemainQty:number,
      /**  The vendor id.  */  
   VendorID:string,
      /**  The vendor name.  */  
   VendName:string,
      /**  The buyer id.  */  
   BuyerID:string,
   RelQtyUOM:string,
   ReceivedQtyUOM:string,
   RemainQtyUOM:string,
      /**  The difference between RelQty and ReceivedQty  */  
   DeviationQty:number,
   AttributeSetID:number,
   ShortDescription:string,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POLateRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The po number.  */  
   PONum:number,
      /**  The po line number.  */  
   POLine:number,
      /**  The po release number.  */  
   PORelNum:number,
      /**  The due date.  */  
   DueDate:string,
      /**  The promise date.  */  
   PromiseDt:string,
      /**  The job number.  */  
   JobNum:string,
      /**  The part number.  */  
   PartNum:string,
      /**  The description of the part.  */  
   PartDescription:string,
      /**  The release quantity.  */  
   RelQty:number,
      /**  The received quantity.  */  
   ReceivedQty:number,
      /**  The remaining quantity  */  
   RemainQty:number,
      /**  The vendor id.  */  
   VendorID:string,
      /**  The vendor name.  */  
   VendName:string,
      /**  The buyer id.  */  
   BuyerID:string,
   RelQtyUOM:string,
   ReceivedQtyUOM:string,
   RemainQtyUOM:string,
      /**  The difference between RelQty and ReceivedQty  */  
   DeviationQty:number,
   AttributeSetID:number,
   ShortDescription:string,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PONewSuggRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The suggestion number.  */  
   SugNum:number,
      /**  The suggestion type.  */  
   SugType:string,
      /**  The buyer id.  */  
   BuyerID:string,
      /**  The po number.  */  
   PONum:number,
      /**  The part number.  */  
   PartNum:string,
   AssemblySeq:number,
   Buy:boolean,
   ClassDescription:string,
   ContractID:string,
   CreateRFQ:boolean,
   DueDate:string,
   DynAttrValueSetShortDesc:string,
   JobNum:string,
   JobSeq:number,
   OrderLine:number,
   OrderNum:number,
   OrderRelNum:number,
   PartNumPartDescription:string,
   PurPoint:string,
   ReqLine:number,
   ReqNum:number,
   Review:boolean,
   RevisionNum:string,
   ShipViaCode:string,
   ShipViaCodeDescription:string,
   VendorID:string,
   VendorNumName:string,
   OrderByDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PORejectRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The transaction id.  */  
   TranID:number,
      /**  The transaction type.  */  
   TranType:string,
      /**  The buyer id.  */  
   BuyerID:string,
      /**  The vendor number.  */  
   VendorNum:number,
      /**  The po number.  */  
   PONum:number,
      /**  The po line number.  */  
   POLine:number,
      /**  The po release number.  */  
   PORelNum:number,
      /**  The transaction date.  */  
   TranDate:string,
      /**  The transaction time  */  
   TranTime:number,
      /**  The vendor name.  */  
   VendName:string,
      /**  Is this po open?  */  
   OpenOrder:boolean,
      /**  Display transaction time formatted Time display.  */  
   DspTranTime:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POThisWeekRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The po number.  */  
   PONum:number,
      /**  The po line number.  */  
   POLine:number,
      /**  The po release number.  */  
   PORelNum:number,
      /**  The due date.  */  
   DueDate:string,
      /**  The promise date.  */  
   PromiseDt:string,
      /**  The job number.  */  
   JobNum:string,
      /**  The part number.  */  
   PartNum:string,
      /**  The description of the part number.  */  
   PartDescription:string,
      /**  The release quantity.  */  
   RelQty:number,
      /**  The received quantity.  */  
   ReceivedQty:number,
      /**  The remaining quantity.  */  
   RemainQty:number,
      /**  The vendor id.  */  
   VendorID:string,
      /**  The vendor name.  */  
   VendName:string,
      /**  The buyer id.  */  
   BuyerID:string,
   RelQtyUOM:string,
   ReceivedQtyUOM:string,
   RemainQtyUOM:string,
      /**  The difference between RelQty and ReceivedQty  */  
   DeviationQty:number,
   AttributeSetID:number,
   ShortDescription:string,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POTodayRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The po number.  */  
   PONum:number,
      /**  The po line number.  */  
   POLine:number,
      /**  The po release number.  */  
   PORelNum:number,
      /**  The due date.  */  
   DueDate:string,
      /**  The promise date.  */  
   PromiseDt:string,
      /**  The job number.  */  
   JobNum:string,
      /**  The part number.  */  
   PartNum:string,
      /**  The description of the part number.  */  
   PartDescription:string,
      /**  The release quantity.  */  
   RelQty:number,
      /**  The received quantity.  */  
   ReceivedQty:number,
      /**  The remaining quantity.  */  
   RemainQty:number,
      /**  The vendor id.  */  
   VendorID:string,
      /**  The vendor name.  */  
   VendName:string,
      /**  The buyer id.  */  
   BuyerID:string,
   RelQtyUOM:string,
   ReceivedQtyUOM:string,
   RemainQtyUOM:string,
      /**  The difference between RelQty and ReceivedQty  */  
   DeviationQty:number,
   AttributeSetID:number,
   ShortDescription:string,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_POTotalRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The buyer id.  */  
   BuyerID:string,
      /**  The total count of pos for this buyer.  */  
   TotalPOCnt:number,
      /**  The buyer name.  */  
   BuyerName:string,
      /**  Number of POs that require approval  */  
   TotalApproval:number,
      /**  Number of POs with a due date greater than the last day of the current week  */  
   TotalFuture:number,
      /**  Number of POs with a due date earlier than todays date  */  
   TotalLate:number,
      /**  Number of POs that have been rejected  */  
   TotalReject:number,
      /**  Number of POs with due date greater than today but less than the last day of the week  */  
   TotalThisWeek:number,
      /**  Number of POs with a due date of today  */  
   TotalToday:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQFutureRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The rfq number.  */  
   RFQNum:number,
      /**  Is the rfq open?  */  
   OpenRFQ:boolean,
      /**  The rfq date.  */  
   RFQDate:string,
      /**  The rfq due date.  */  
   RFQDueDate:string,
      /**  The buyer id.  */  
   BuyerID:string,
      /**  The comment text.  */  
   CommentText:string,
      /**  Is rfq ready to be printed?  */  
   ReadyToPrint:boolean,
      /**  The respond date.  */  
   RespondDate:string,
      /**  The decision date.  */  
   DecisionDate:string,
      /**  Post to web?  */  
   PostToWeb:boolean,
      /**  The post date.  */  
   PostDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQOverdueRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The rfq number.  */  
   RFQNum:number,
      /**  Is the rfq open?  */  
   OpenRFQ:boolean,
      /**  The rfq date.  */  
   RFQDate:string,
      /**  The rfq due date.  */  
   RFQDueDate:string,
      /**  The buyer id.  */  
   BuyerID:string,
      /**  The comment text.  */  
   CommentText:string,
      /**  Is rfq ready to be printed?  */  
   ReadyToPrint:boolean,
      /**  The respond date.  */  
   RespondDate:string,
      /**  The decision date.  */  
   DecisionDate:string,
      /**  Post to web?  */  
   PostToWeb:boolean,
      /**  The post date.  */  
   PostDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQReadyRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The rfq number.  */  
   RFQNum:number,
      /**  The rfq line number.  */  
   RFQLine:number,
      /**  The rfq date.  */  
   RFQDate:string,
      /**  The part number.  */  
   PartNum:string,
      /**  The part number description.  */  
   PartDescription:string,
      /**  The rfq due date.  */  
   RFQDueDate:string,
      /**  The respond date.  */  
   RespondDate:string,
      /**  The decision date.  */  
   DecisionDate:string,
      /**  The buyer id.  */  
   BuyerID:string,
      /**  The number of received responses.  */  
   RcvdRspns:number,
      /**  The number of minimum needed responses.  */  
   NeededRspns:number,
      /**  The total responses.  */  
   TotRspns:number,
   ItemType:string,
   QuoteNum:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQSuggBWBRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The suggestion number.  */  
   SugNum:number,
      /**  The line description.  */  
   LineDesc:string,
      /**  The ium.  */  
   IUM:string,
      /**  The part number.  */  
   PartNum:string,
      /**  The description for the part number.  */  
   PartDescription:string,
      /**  The part revision number.  */  
   RevisionNum:string,
      /**  The comment text.  */  
   CommentText:string,
      /**  The class.  */  
   Class:string,
      /**  The job number.  */  
   JobNum:string,
      /**  The quote number.  */  
   QuoteNum:number,
      /**  The quote line number.  */  
   QuoteLine:number,
      /**  The assembly sequence.  */  
   AssemblySeq:number,
      /**  The job sequence.  */  
   JobSeq:number,
      /**  The item type.  */  
   ItemType:string,
      /**  The vendor number.  */  
   VendorNum:number,
      /**  The vendor quote requirements.  */  
   RFQVendQuotes:number,
      /**  Process the rfq?  */  
   ProcessRFQ:boolean,
      /**  The vendor id.  */  
   VendorID:string,
      /**  The source.  */  
   Source:string,
      /**  The buyer id.  */  
   BuyerID:string,
   QtyList:string,
   GlbSuggestion:boolean,
   GlbCompany:string,
      /**  The purchase point.  */  
   PurPoint:string,
   OpCode:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQSuggVendRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The vendor number.  */  
   VendorNum:number,
      /**  The vendor id.  */  
   VendorID:string,
      /**  The vendor name.  */  
   VendName:string,
      /**  The purchase point.  */  
   PurPoint:string,
      /**  Approved?  */  
   Approved:boolean,
      /**  The suggestion number.  */  
   SugNum:number,
      /**  The buyer id.  */  
   BuyerID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQThisWeekRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The rfq number.  */  
   RFQNum:number,
      /**  Is the rfq open?  */  
   OpenRFQ:boolean,
      /**  The rfq date.  */  
   RFQDate:string,
      /**  The rfq due date.  */  
   RFQDueDate:string,
      /**  The buyer id.  */  
   BuyerID:string,
      /**  The comment text.  */  
   CommentText:string,
      /**  Is the rfq ready to be printed?  */  
   ReadyToPrint:boolean,
      /**  The respond date.  */  
   RespondDate:string,
      /**  The decision date.  */  
   DecisionDate:string,
      /**  Post to web?  */  
   PostToWeb:boolean,
      /**  The post date.  */  
   PostDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQTodayRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The rfq number.  */  
   RFQNum:number,
      /**  Is the rfq open?  */  
   OpenRFQ:boolean,
      /**  The rfq date.  */  
   RFQDate:string,
      /**  The rfq due date.  */  
   RFQDueDate:string,
      /**  The buyer id.  */  
   BuyerID:string,
      /**  The comment text.  */  
   CommentText:string,
      /**  Is the rfq ready to be printed?  */  
   ReadyToPrint:boolean,
      /**  The respond date.  */  
   RespondDate:string,
      /**  The decision date.  */  
   DecisionDate:string,
      /**  Post to web?  */  
   PostToWeb:boolean,
      /**  The post date.  */  
   PostDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQTotalRow{
      /**  The company indentifier.  */  
   Company:string,
      /**  The buyer id.  */  
   BuyerID:string,
      /**  The total count of rfqs for this buyer.  */  
   TotalRFQCnt:number,
      /**  The buyer name.  */  
   BuyerName:string,
      /**  The descision date  */  
   DecisionDate:string,
      /**  The due date  */  
   DueDate:string,
      /**  Comment field for RFQHead when an RFQ Suggestion is generated into an RFQ.  Used in BuyerWorkbench.  */  
   CommentText:string,
   PostToWeb:boolean,
      /**  The respond date  */  
   RespondDate:string,
      /**  Number of RFQs with a due date greater than the last day of the current week  */  
   TotalFuture:number,
      /**  Number of RFQs with a due date earlier than todays date  */  
   TotalOverdue:number,
      /**  Number of RFQs that have received supplier responses and are ready to be turned into purchase orders  */  
   TotalReady:number,
      /**  Number of RFQs with due date greater than today but less than the last day of the week  */  
   TotalThisWeek:number,
      /**  Number of RFQs with a due date of today  */  
   TotalToday:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipBuyerID
      @param ds
   */  
export interface Generate_input{
      /**  The buyer id to generate for.  */  
   ipBuyerID:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset[],
}

export interface Generate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BuyerWorkbenchTableset,
}
}

   /** Required : 
      @param ipBuyerID
      @param ipSugNum
      @param ds
   */  
export interface GetNewSuggSupp_input{
      /**  The buyer id to add data for.  */  
   ipBuyerID:string,
      /**  The suggestion number to link suppliers to.  */  
   ipSugNum:number,
   ds:Erp_Tablesets_BuyerWorkbenchTableset[],
}

export interface GetNewSuggSupp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BuyerWorkbenchTableset,
}
}

   /** Required : 
      @param buyerID
   */  
export interface GetSugPOChgCount_input{
      /**  buyerID  */  
   buyerID:string,
}

export interface GetSugPOChgCount_output{
      /**  Count  */  
   returnObj:number,
}

   /** Required : 
      @param buyerID
   */  
export interface GetSugPoDtlCount_input{
      /**  buyerID  */  
   buyerID:string,
}

export interface GetSugPoDtlCount_output{
      /**  Count  */  
   returnObj:number,
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
      @param ipBuyerID
      @param ds
   */  
export interface SelectAll_input{
      /**  The buyer id to select all for.  */  
   ipBuyerID:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset[],
}

export interface SelectAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_BuyerWorkbenchTableset,
}
}

   /** Required : 
      @param sugNum
      @param ipSoldPart
      @param ipPreviousRFQ
      @param ipPriceBreak
      @param ipComplianceList
      @param includeVendAttrList
      @param excludeVendAttrList
      @param ds
   */  
export interface SupplierWizard_input{
      /**  Suggestion number the wizard is running for  */  
   sugNum:number,
      /**  Suppliers have sold us this part?  */  
   ipSoldPart:boolean,
      /**  Suppliers have previously received an RFQ?  */  
   ipPreviousRFQ:boolean,
      /**  Suppliers have provided price break information?  */  
   ipPriceBreak:boolean,
      /**  Compliance list  */  
   ipComplianceList:string,
      /**  The include vendor attributes list  */  
   includeVendAttrList:string,
      /**  The exclude vendor attributes list  */  
   excludeVendAttrList:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset[],
}

export interface SupplierWizard_output{
parameters : {
      /**  output parameters  */  
   opStatusMsg:string,
   ds:Erp_Tablesets_BuyerWorkbenchTableset,
}
}

