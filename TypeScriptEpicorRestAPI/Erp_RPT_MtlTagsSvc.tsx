import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.RPT.MtlTagsSvc
// Description: MtlTagsSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/$metadata", {
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
   Summary: Invoke method CalculateTotals
   Description: Calculate TagNumber and TagQty based on the ItemTags data
   OperationID: CalculateTotals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateTotals(requestBody:CalculateTotals_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateTotals_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/CalculateTotals", {
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
         resolve(data as CalculateTotals_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReturnTempTable
   Description: ReturnTempTable - Returns ItemTags table based on QtyPer and TotalQty
   OperationID: ReturnTempTable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReturnTempTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReturnTempTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReturnTempTable(requestBody:ReturnTempTable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReturnTempTable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/ReturnTempTable", {
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
         resolve(data as ReturnTempTable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReturnTempTableWithAttributeSetData
   Description: ReturnTempTableWithAttributeSetData - Returns ItemTags table based on QtyPer and TotalQty, considering Attribute Sets.
   OperationID: ReturnTempTableWithAttributeSetData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReturnTempTableWithAttributeSetData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReturnTempTableWithAttributeSetData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReturnTempTableWithAttributeSetData(requestBody:ReturnTempTableWithAttributeSetData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReturnTempTableWithAttributeSetData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/ReturnTempTableWithAttributeSetData", {
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
         resolve(data as ReturnTempTableWithAttributeSetData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalculateNumberOfPieces
   Description: Returns the Number of Pieces calculated based in QtyPer and the other parameters received.
   OperationID: CalculateNumberOfPieces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateNumberOfPieces(requestBody:CalculateNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/CalculateNumberOfPieces", {
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
         resolve(data as CalculateNumberOfPieces_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewItemTags
   Description: Creates a new record in the ItemsTags dataset
   OperationID: GetNewItemTags
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewItemTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewItemTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewItemTags(requestBody:GetNewItemTags_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewItemTags_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/GetNewItemTags", {
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
         resolve(data as GetNewItemTags_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewParametersWithIntialValueIn
   Description: Executes GetNewParameters and sets values from initialValueIn based on the UI that launched the report.
   OperationID: GetNewParametersWithIntialValueIn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewParametersWithIntialValueIn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewParametersWithIntialValueIn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewParametersWithIntialValueIn(requestBody:GetNewParametersWithIntialValueIn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewParametersWithIntialValueIn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/GetNewParametersWithIntialValueIn", {
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
         resolve(data as GetNewParametersWithIntialValueIn_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRcvDtlAttributeValueParameters
   Description: Returns a set of Attribute Set string list parameters from RcvDtlAttrValueSet. Created to handle Receive Entry and Receive Container Entry multiple Attribute Sets special case.
   OperationID: GetRcvDtlAttributeValueParameters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRcvDtlAttributeValueParameters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRcvDtlAttributeValueParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRcvDtlAttributeValueParameters(requestBody:GetRcvDtlAttributeValueParameters_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRcvDtlAttributeValueParameters_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/GetRcvDtlAttributeValueParameters", {
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
         resolve(data as GetRcvDtlAttributeValueParameters_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAttributeSetList
   Description: Return a delimited list of attrValueSeq'attributeSetShortDescription
   OperationID: GetAttributeSetList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAttributeSetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributeSetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAttributeSetList(requestBody:GetAttributeSetList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAttributeSetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/GetAttributeSetList", {
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
         resolve(data as GetAttributeSetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedItemQtyWithItemTags
   Description: Invoked when ItemQty in the ItemTags grid is changed.  Sets DispNumberOfPieces and invokes CalculateTotals.
   OperationID: OnChangedItemQtyWithItemTags
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedItemQtyWithItemTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedItemQtyWithItemTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedItemQtyWithItemTags(requestBody:OnChangedItemQtyWithItemTags_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedItemQtyWithItemTags_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/OnChangedItemQtyWithItemTags", {
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
         resolve(data as OnChangedItemQtyWithItemTags_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeValueSeq
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeValueSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeValueSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeValueSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeValueSeq(requestBody:OnChangingAttributeValueSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingAttributeValueSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/OnChangingAttributeValueSeq", {
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
         resolve(data as OnChangingAttributeValueSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeValueSeqWithItemTags
   Description: Invoked when AttributeValueSeq is changed and updates fields based on selected value
   OperationID: OnChangingAttributeValueSeqWithItemTags
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeValueSeqWithItemTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeValueSeqWithItemTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeValueSeqWithItemTags(requestBody:OnChangingAttributeValueSeqWithItemTags_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingAttributeValueSeqWithItemTags_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/OnChangingAttributeValueSeqWithItemTags", {
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
         resolve(data as OnChangingAttributeValueSeqWithItemTags_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPieces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:OnChangingNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/OnChangingNumberOfPieces", {
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
         resolve(data as OnChangingNumberOfPieces_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPiecesWithItemTags
   Description: Invokes OnChangingNumberOfPieces and refreshes the ItemTag data
   OperationID: OnChangingNumberOfPiecesWithItemTags
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPiecesWithItemTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPiecesWithItemTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPiecesWithItemTags(requestBody:OnChangingNumberOfPiecesWithItemTags_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumberOfPiecesWithItemTags_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/OnChangingNumberOfPiecesWithItemTags", {
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
         resolve(data as OnChangingNumberOfPiecesWithItemTags_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingQtyPer
   Description: Call this method when the Qty Per changes to calculate a new tran qty
   OperationID: OnChangingQtyPer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingQtyPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingQtyPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingQtyPer(requestBody:OnChangingQtyPer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingQtyPer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/OnChangingQtyPer", {
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
         resolve(data as OnChangingQtyPer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingQtyPerWithItemTags
   Description: Invokes OnChangingQtyPer and refreshes the ItemTag data
   OperationID: OnChangingQtyPerWithItemTags
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingQtyPerWithItemTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingQtyPerWithItemTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingQtyPerWithItemTags(requestBody:OnChangingQtyPerWithItemTags_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingQtyPerWithItemTags_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/OnChangingQtyPerWithItemTags", {
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
         resolve(data as OnChangingQtyPerWithItemTags_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetTokenList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/GetTokenList" + params, {
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
         resolve(data as GetTokenList_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetTokenValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/GetTokenValue" + params, {
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
         resolve(data as GetTokenValue_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetRptArchiveList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/GetRptArchiveList", {
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
         resolve(data as GetRptArchiveList_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SubmitToAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitToAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitToAgent(requestBody:SubmitToAgent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SubmitToAgent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/SubmitToAgent", {
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
         resolve(data as SubmitToAgent_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaults(requestBody:GetDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/GetDefaults", {
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
         resolve(data as GetDefaults_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetNewParameters_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/GetNewParameters", {
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
         resolve(data as GetNewParameters_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetParamsFromAgent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/GetParamsFromAgent" + params, {
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
         resolve(data as GetParamsFromAgent_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetParamTaskDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamTaskDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetParamTaskDef(requestBody:GetParamTaskDef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetParamTaskDef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/GetParamTaskDef", {
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
         resolve(data as GetParamTaskDef_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemoveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveDefaults(requestBody:RemoveDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/RemoveDefaults", {
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
         resolve(data as RemoveDefaults_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RunDirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunDirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunDirect(requestBody:RunDirect_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RunDirect_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/RunDirect", {
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
         resolve(data as RunDirect_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveDefaults(requestBody:SaveDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/SaveDefaults", {
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
         resolve(data as SaveDefaults_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveProcessTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveProcessTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveProcessTask(requestBody:SaveProcessTask_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveProcessTask_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.MtlTagsSvc/SaveProcessTask", {
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
         resolve(data as SaveProcessTask_output)
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
      @param partNum
      @param qtyPer
      @param uom
      @param attributeSetID
   */  
export interface CalculateNumberOfPieces_input{
   partNum:string,
   qtyPer:number,
   uom:string,
   attributeSetID:number,
}

export interface CalculateNumberOfPieces_output{
   returnObj:number,
}

   /** Required : 
      @param dsItemTags
      @param ds
   */  
export interface CalculateTotals_input{
   dsItemTags:Erp_Tablesets_ItemTagsTableset[],
   ds:Erp_Tablesets_MtlTagsTableset[],
}

export interface CalculateTotals_output{
parameters : {
      /**  output parameters  */  
   dsItemTags:Erp_Tablesets_ItemTagsTableset,
   ds:Erp_Tablesets_MtlTagsTableset,
}
}

export interface Erp_Tablesets_ItemTagsRow{
   ItemQty:number,
   ItemTags:number,
   ItemUOM:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   AttributeSetShortDescription:string,
      /**  Unique identifier for this Attribute Value for this receipt detail.  */  
   AttributeValueSeq:number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ItemTagsTableset{
   ItemTags:Erp_Tablesets_ItemTagsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MtlTagsParamRow{
   TagFormat:string,
   TotalQty:number,
   QtyPer:number,
   PartNum:string,
   Revision:string,
   PartDesc:string,
   UnitOfMeasure:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   PONum:number,
   POLine:number,
   PORel:number,
   VendorNum:number,
   PurPoint:string,
   RefJob:string,
   RefAssemblySeq:number,
   RefMtlSeq:number,
   NonConfTranID:number,
   ReasonCode:string,
   ReasonType:string,
   Comment:string,
   WarehouseCode:string,
   BinNum:string,
   LotNum:string,
   ItemTags:string,
      /**  Indicates the type of the reference: M ? Material (JobMtl), O / Empty ? Operation (JobOper)  */  
   JobSeqType:string,
      /**  Flag to indicate if Bar Codes are printed on labels.  Defaulted to the Company level flag.  */  
   BarCodes:boolean,
      /**  Legal Number  */  
   LegalNumber:string,
   PCID:string,
   DMRNum:number,
      /**  The quantity of parts being tagged.  */  
   TagQty:number,
      /**  The number of tags being printed  */  
   TagNumber:number,
      /**  Number assigned by the system to uniquely identify the record.  */  
   MtlQueueSeq:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   AttributeSetShortDescription:string,
      /**  Unique identifier for this Attribute Value for this receipt detail.  */  
   AttributeValueSeq:number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
      /**  A List of unique identifiers of the related Dynamic Attribute Sets.  */  
   AttributeSetIDList:string,
      /**  A List of Short Description of the Attribute Sets.  */  
   AttributeSetShortDescList:string,
      /**  A list of unique identifiers for this Attribute Value in receipt detail.  */  
   AttributeValueSeqList:string,
      /**  A List of Number of pieces for inventory attribute tracked parts.  */  
   NumberOfPiecesList:string,
   QtyPerContainerList:string,
   AttributeSetClassID:string,
   TotalQtyUOM:string,
   AttributeSetTotalQtyList:string,
   AttributeSetUOMList:string,
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

export interface Erp_Tablesets_MtlTagsTableset{
   MtlTagsParam:Erp_Tablesets_MtlTagsParamRow[],
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
      @param attributeValueSeqList
      @param attributeSetShortDescList
   */  
export interface GetAttributeSetList_input{
   attributeValueSeqList:string,
   attributeSetShortDescList:string,
}

export interface GetAttributeSetList_output{
parameters : {
      /**  output parameters  */  
   attributeSetList:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetDefaults_input{
   ds:Erp_Tablesets_MtlTagsTableset[],
}

export interface GetDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MtlTagsTableset,
}
}

   /** Required : 
      @param ds
      @param dsItemTags
   */  
export interface GetNewItemTags_input{
   ds:Erp_Tablesets_MtlTagsTableset[],
   dsItemTags:Erp_Tablesets_ItemTagsTableset[],
}

export interface GetNewItemTags_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MtlTagsTableset,
   dsItemTags:Erp_Tablesets_ItemTagsTableset,
}
}

   /** Required : 
      @param initialValueIn
      @param launchedFrom
      @param ds
   */  
export interface GetNewParametersWithIntialValueIn_input{
   initialValueIn:string,
   launchedFrom:string,
   ds:Erp_Tablesets_ItemTagsTableset[],
}

export interface GetNewParametersWithIntialValueIn_output{
   returnObj:Erp_Tablesets_MtlTagsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ItemTagsTableset,
}
}

export interface GetNewParameters_output{
   returnObj:Erp_Tablesets_MtlTagsTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetParamTaskDef_input{
   ds:Erp_Tablesets_MtlTagsTableset[],
}

export interface GetParamTaskDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MtlTagsTableset,
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
   returnObj:Erp_Tablesets_MtlTagsTableset[],
}

   /** Required : 
      @param company
      @param vendorNum
      @param purPoint
      @param packSlip
      @param packLine
      @param partNum
   */  
export interface GetRcvDtlAttributeValueParameters_input{
   company:string,
   vendorNum:number,
   purPoint:string,
   packSlip:string,
   packLine:number,
   partNum:string,
}

export interface GetRcvDtlAttributeValueParameters_output{
parameters : {
      /**  output parameters  */  
   attributeValueSeqList:string,
   attributeSetIDList:string,
   attributeSetShortDescriptionList:string,
   numberOfPiecesList:string,
   qtyPerContainerList:string,
   attributeValueTotalList:string,
   attributeUOMList:string,
}
}

export interface GetRptArchiveList_output{
   returnObj:string,
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
      @param sysRowID
      @param ds
      @param dsItemTags
   */  
export interface OnChangedItemQtyWithItemTags_input{
   sysRowID:string,
   ds:Erp_Tablesets_MtlTagsTableset[],
   dsItemTags:Erp_Tablesets_ItemTagsTableset[],
}

export interface OnChangedItemQtyWithItemTags_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MtlTagsTableset,
   dsItemTags:Erp_Tablesets_ItemTagsTableset,
}
}

   /** Required : 
      @param attributeValueSeq
      @param ds
      @param dsItemTags
   */  
export interface OnChangingAttributeValueSeqWithItemTags_input{
   attributeValueSeq:number,
   ds:Erp_Tablesets_MtlTagsTableset[],
   dsItemTags:Erp_Tablesets_ItemTagsTableset[],
}

export interface OnChangingAttributeValueSeqWithItemTags_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MtlTagsTableset,
}
}

   /** Required : 
      @param attributeValueSeq
      @param ds
   */  
export interface OnChangingAttributeValueSeq_input{
   attributeValueSeq:number,
   ds:Erp_Tablesets_MtlTagsTableset[],
}

export interface OnChangingAttributeValueSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MtlTagsTableset,
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
      @param dsItemTags
   */  
export interface OnChangingNumberOfPiecesWithItemTags_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_MtlTagsTableset[],
   dsItemTags:Erp_Tablesets_ItemTagsTableset[],
}

export interface OnChangingNumberOfPiecesWithItemTags_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MtlTagsTableset,
   dsItemTags:Erp_Tablesets_ItemTagsTableset,
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_MtlTagsTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MtlTagsTableset,
}
}

   /** Required : 
      @param qtyPer
      @param ds
      @param dsItemTags
   */  
export interface OnChangingQtyPerWithItemTags_input{
   qtyPer:number,
   ds:Erp_Tablesets_MtlTagsTableset[],
   dsItemTags:Erp_Tablesets_ItemTagsTableset[],
}

export interface OnChangingQtyPerWithItemTags_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MtlTagsTableset,
   dsItemTags:Erp_Tablesets_ItemTagsTableset,
}
}

   /** Required : 
      @param qtyPer
      @param ds
   */  
export interface OnChangingQtyPer_input{
   qtyPer:number,
   ds:Erp_Tablesets_MtlTagsTableset[],
}

export interface OnChangingQtyPer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MtlTagsTableset,
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
      @param vItemQty
      @param vTranQty
      @param vUOM
      @param partNum
      @param attributeValueSeq
      @param attributeValueSeqList
      @param attributeSetIDList
      @param atrributeSetShortDescList
      @param numberOfPiecesList
      @param itemQtyList
      @param itemTagsList
      @param attributeValueTotalList
      @param attributeUOMList
   */  
export interface ReturnTempTableWithAttributeSetData_input{
   vItemQty:number,
   vTranQty:number,
   vUOM:string,
   partNum:string,
   attributeValueSeq:number,
   attributeValueSeqList:string,
   attributeSetIDList:string,
   atrributeSetShortDescList:string,
   numberOfPiecesList:string,
   itemQtyList:string,
   itemTagsList:string,
   attributeValueTotalList:string,
   attributeUOMList:string,
}

export interface ReturnTempTableWithAttributeSetData_output{
   returnObj:Erp_Tablesets_ItemTagsTableset[],
}

   /** Required : 
      @param vItemQty
      @param vTranQty
      @param vUOM
   */  
export interface ReturnTempTable_input{
   vItemQty:number,
   vTranQty:number,
   vUOM:string,
}

export interface ReturnTempTable_output{
   returnObj:Erp_Tablesets_ItemTagsTableset[],
}

   /** Required : 
      @param ds
   */  
export interface RunDirect_input{
   ds:Erp_Tablesets_MtlTagsTableset[],
}

export interface RunDirect_output{
}

   /** Required : 
      @param ds
   */  
export interface SaveDefaults_input{
   ds:Erp_Tablesets_MtlTagsTableset[],
}

export interface SaveDefaults_output{
}

   /** Required : 
      @param maintProgram
      @param ds
   */  
export interface SaveProcessTask_input{
   maintProgram:string,
   ds:Erp_Tablesets_MtlTagsTableset[],
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
   ds:Erp_Tablesets_MtlTagsTableset[],
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

