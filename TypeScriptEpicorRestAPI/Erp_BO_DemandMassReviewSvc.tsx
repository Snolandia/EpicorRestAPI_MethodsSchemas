import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.DemandMassReviewSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/$metadata", {
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
   Summary: Invoke method CloseAll
   Description: Purpose:
Parameters:  none
Notes:
<param>The Demand Mass Review Data Set</param>
   OperationID: CloseAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CloseAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseAll(requestBody:CloseAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CloseAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/CloseAll", {
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
         resolve(data as CloseAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CloseAllPart
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipGroupID">Demand Mass Review Current Group.</param><param name="ds">The Demand Mass Review Data Set</param>
   OperationID: CloseAllPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CloseAllPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseAllPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseAllPart(requestBody:CloseAllPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CloseAllPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/CloseAllPart", {
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
         resolve(data as CloseAllPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CloseDemand
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipGroupID">Demand Mass Review Current Group.</param><param name="ds">The Demand Mass Review Data Set</param>
   OperationID: CloseDemand
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CloseDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseDemand(requestBody:CloseDemand_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CloseDemand_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/CloseDemand", {
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
         resolve(data as CloseDemand_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CloseRejectedDemand
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipGroupID">Demand Mass Review Current Group.</param><param name="ds">The Demand Mass Review Data Set</param>
   OperationID: CloseRejectedDemand
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CloseRejectedDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseRejectedDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseRejectedDemand(requestBody:CloseRejectedDemand_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CloseRejectedDemand_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/CloseRejectedDemand", {
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
         resolve(data as CloseRejectedDemand_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CloseWorkList
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipGroupID">Demand Mass Review Current Group.</param><param name="ds">The Demand Mass Review Data Set</param>
   OperationID: CloseWorkList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CloseWorkList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseWorkList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseWorkList(requestBody:CloseWorkList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CloseWorkList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/CloseWorkList", {
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
         resolve(data as CloseWorkList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteDemand
   Description: Delete the schedules related to the selected Part/Demand. Demand Mass Review
summarize demands, on that case will we be deleting all schedules that were
included on that selected record. If a schedule is selected for another
Group different than the current, we'll check if it is not locked and if not
we can delete the schedule.
   OperationID: DeleteDemand
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteDemand(requestBody:DeleteDemand_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteDemand_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/DeleteDemand", {
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
         resolve(data as DeleteDemand_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteGroup
   OperationID: DeleteGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteGroup(requestBody:DeleteGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/DeleteGroup", {
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
         resolve(data as DeleteGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDemandMassReview
   Description: Call this method when the user selects parts or demands to review.  This
method populates the Epicor.Mfg.BO.DemandMassReviewDataSet dataset for
criteria selected.
   OperationID: GetDemandMassReview
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDemandMassReview_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDemandMassReview_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDemandMassReview(requestBody:GetDemandMassReview_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDemandMassReview_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/GetDemandMassReview", {
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
         resolve(data as GetDemandMassReview_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMassReviewDtl
   Description: Call this method to get the demand details for a part when a different part
is selected.
   OperationID: GetMassReviewDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetMassReviewDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMassReviewDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMassReviewDtl(requestBody:GetMassReviewDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMassReviewDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/GetMassReviewDtl", {
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
         resolve(data as GetMassReviewDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MatchAllForDemand
   Description: This method will perform the default matching of Demand Schedules
to Order Releases for a demand.
   OperationID: MatchAllForDemand
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MatchAllForDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchAllForDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MatchAllForDemand(requestBody:MatchAllForDemand_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MatchAllForDemand_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/MatchAllForDemand", {
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
         resolve(data as MatchAllForDemand_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MatchAllForPart
   Description: This method will perform the default matching of Demand Schedules
to Order Releases for a part.
   OperationID: MatchAllForPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MatchAllForPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchAllForPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MatchAllForPart(requestBody:MatchAllForPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MatchAllForPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/MatchAllForPart", {
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
         resolve(data as MatchAllForPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeUOM
   Description: Updates the On Hand Quantity according to the UOM
method populates the Epicor.Mfg.BO.DemandMassReviewDataSet dataset for
criteria selected.
   OperationID: OnChangeUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUOM(requestBody:OnChangeUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/OnChangeUOM", {
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
         resolve(data as OnChangeUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessingSelectAll
   Description: This method will set all demands that have not been posted to be ready for processing.
   OperationID: ProcessingSelectAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessingSelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessingSelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessingSelectAll(requestBody:ProcessingSelectAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessingSelectAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/ProcessingSelectAll", {
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
         resolve(data as ProcessingSelectAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessingSelectAllForPart
   Description: This method will mark all demands for a part to be ready for processing.
   OperationID: ProcessingSelectAllForPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessingSelectAllForPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessingSelectAllForPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessingSelectAllForPart(requestBody:ProcessingSelectAllForPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessingSelectAllForPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/ProcessingSelectAllForPart", {
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
         resolve(data as ProcessingSelectAllForPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessingSelectByDemand
   Description: This method will mark a demand as be ready for processing.
   OperationID: ProcessingSelectByDemand
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessingSelectByDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessingSelectByDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessingSelectByDemand(requestBody:ProcessingSelectByDemand_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessingSelectByDemand_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/ProcessingSelectByDemand", {
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
         resolve(data as ProcessingSelectByDemand_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessingSelectWorkList
   Description: This method will mark all demands for the work list to be ready for processing.
   OperationID: ProcessingSelectWorkList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessingSelectWorkList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessingSelectWorkList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessingSelectWorkList(requestBody:ProcessingSelectWorkList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessingSelectWorkList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/ProcessingSelectWorkList", {
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
         resolve(data as ProcessingSelectWorkList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RejectAllForDemand
   Description: This method will mark a demand as rejected.
   OperationID: RejectAllForDemand
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RejectAllForDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectAllForDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RejectAllForDemand(requestBody:RejectAllForDemand_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RejectAllForDemand_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/RejectAllForDemand", {
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
         resolve(data as RejectAllForDemand_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RejectAllForPart
   Description: This method will mark all demands for a part as rejected.
   OperationID: RejectAllForPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RejectAllForPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RejectAllForPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RejectAllForPart(requestBody:RejectAllForPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RejectAllForPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/RejectAllForPart", {
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
         resolve(data as RejectAllForPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnmatchAll
   Description: Unmatch all the demand entries previously loaded
   OperationID: UnmatchAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnmatchAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnmatchAll(requestBody:UnmatchAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnmatchAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DemandMassReviewSvc/UnmatchAll", {
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
         resolve(data as UnmatchAll_output)
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
      @param ipGroupID
      @param ds
   */  
export interface CloseAllPart_input{
   ipGroupID:string,
   ds:Erp_Tablesets_DemandMassReviewTableset[],
}

export interface CloseAllPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandMassReviewTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CloseAll_input{
   ds:Erp_Tablesets_DemandMassReviewTableset[],
}

export interface CloseAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandMassReviewTableset,
}
}

   /** Required : 
      @param ipGroupID
      @param ds
   */  
export interface CloseDemand_input{
   ipGroupID:string,
   ds:Erp_Tablesets_DemandMassReviewTableset[],
}

export interface CloseDemand_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandMassReviewTableset,
}
}

   /** Required : 
      @param ipGroupID
      @param ds
   */  
export interface CloseRejectedDemand_input{
   ipGroupID:string,
   ds:Erp_Tablesets_DemandMassReviewTableset[],
}

export interface CloseRejectedDemand_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandMassReviewTableset,
}
}

   /** Required : 
      @param ipGroupID
      @param ds
   */  
export interface CloseWorkList_input{
   ipGroupID:string,
   ds:Erp_Tablesets_DemandMassReviewTableset[],
}

export interface CloseWorkList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandMassReviewTableset,
}
}

   /** Required : 
      @param ds
      @param ipGroupID
   */  
export interface DeleteDemand_input{
   ds:Erp_Tablesets_DemandMassReviewTableset[],
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
}

export interface DeleteDemand_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandMassReviewTableset,
}
}

   /** Required : 
      @param ipGroupID
   */  
export interface DeleteGroup_input{
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
}

export interface DeleteGroup_output{
parameters : {
      /**  output parameters  */  
   cOutputMsg:string,
}
}

export interface Erp_Tablesets_DemandMassInputsRow{
   Company:string,
   PartNum:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   Description:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandMassInputsTableset{
   DemandMassInputs:Erp_Tablesets_DemandMassInputsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DemandMassReviewDtlRow{
   Company:string,
   PrimaryField:string,
   PrimaryFieldDtl:string,
   CustID:string,
   CustomerName:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   DemandContract:string,
   DemandPONum:string,
   PartNum:string,
   PartDesc:string,
      /**  .  */  
   MDPV:number,
   PartOnHandQty:number,
   PartAvailableQty:number,
   BalanceDifference:number,
   CostQtyDifference:number,
   CurBalance:number,
   CurDemandQty:number,
   ProposedBalance:number,
   ProposedDemandQty:number,
   QuantityDifference:number,
   SelectForProcess:boolean,
   Reject:boolean,
   ShipByDate:string,
   RecordType:string,
   DemandContractLine:number,
   DemandDtlSeq:number,
   ContractUnitPrice:number,
   DemandUnitPrice:number,
      /**  Current Demand UOM  */  
   CurDemandQtyUOM:string,
      /**  Proposed Demand UOM  */  
   ProposedDemandQtyUOM:string,
   Closed:boolean,
   RejectedBySystem:boolean,
   DemandType:string,
      /**  All Demand Reviews belong to a group until the group is posted. The GroupID is assigned by the user.  */  
   GroupID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandMassReviewRow{
   Company:string,
      /**  The primary field for this table.  It will have either the Part Number or a concatenated string of demand contract name and po.  */  
   PrimaryField:string,
      /**  The type of record this is.  Options are (P)art or (C)ontract/PO.  */  
   RecordType:string,
   CustID:string,
   CustomerName:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   DemandPONum:string,
   PartNum:string,
   MDPV:number,
   OnHandQty:number,
   AvailableQty:number,
   DemandContract:string,
   SelectForProcess:boolean,
   Reject:boolean,
   Description:string,
      /**  Part UOM  */  
   UOM:string,
      /**  Available Quantity UOM  */  
   AvailableQtyUOM:string,
      /**  MDPV UOM  */  
   MDPVUOM:string,
      /**  On Hand Quantity UOM  */  
   OnHandQtyUOM:string,
   Closed:boolean,
   RejectedBySystem:boolean,
   GroupID:string,
   TrackUOM:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DemandMassReviewTableset{
   DemandMassReview:Erp_Tablesets_DemandMassReviewRow[],
   DemandMassReviewDtl:Erp_Tablesets_DemandMassReviewDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipGroupID
      @param ds
   */  
export interface GetDemandMassReview_input{
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
   ds:Erp_Tablesets_DemandMassInputsTableset[],
}

export interface GetDemandMassReview_output{
   returnObj:Erp_Tablesets_DemandMassReviewTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandMassInputsTableset,
   cOutputMsg:string,
}
}

   /** Required : 
      @param ipGroupID
      @param cPrimaryField
      @param lFirm
      @param lUnfirm
      @param lForecast
      @param ds
   */  
export interface GetMassReviewDtl_input{
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
      /**  The primary field value of DemandMassReview  */  
   cPrimaryField:string,
      /**  Include Firm Demand Schedules?  */  
   lFirm:boolean,
      /**  Include Unfirm Demand Schedules?  */  
   lUnfirm:boolean,
      /**  Include Forecast Demand Schedules?  */  
   lForecast:boolean,
   ds:Erp_Tablesets_DemandMassReviewTableset[],
}

export interface GetMassReviewDtl_output{
parameters : {
      /**  output parameters  */  
   cOutputMsg:string,
   ds:Erp_Tablesets_DemandMassReviewTableset,
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
      @param ipGroupID
      @param iDemandContractNum
      @param iDemandHeadSeq
   */  
export interface MatchAllForDemand_input{
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
      /**  The Contract Number to process  */  
   iDemandContractNum:number,
      /**  The Demand Head identifier to process  */  
   iDemandHeadSeq:number,
}

export interface MatchAllForDemand_output{
parameters : {
      /**  output parameters  */  
   cOutputMessage:string,
   lMatched:boolean,
}
}

   /** Required : 
      @param ipGroupID
      @param cPartNum
   */  
export interface MatchAllForPart_input{
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
      /**  The Part Number to process  */  
   cPartNum:string,
}

export interface MatchAllForPart_output{
parameters : {
      /**  output parameters  */  
   cOutputMessage:string,
}
}

   /** Required : 
      @param cPrimaryField
      @param ds
   */  
export interface OnChangeUOM_input{
      /**  The primary field value of DemandMassReview  */  
   cPrimaryField:string,
   ds:Erp_Tablesets_DemandMassReviewTableset[],
}

export interface OnChangeUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandMassReviewTableset,
}
}

   /** Required : 
      @param ipGroupID
      @param cPartNum
      @param cSelectType
   */  
export interface ProcessingSelectAllForPart_input{
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
      /**  The Part Number to process  */  
   cPartNum:string,
      /**  (S)elect or (U)nselect  */  
   cSelectType:string,
}

export interface ProcessingSelectAllForPart_output{
parameters : {
      /**  output parameters  */  
   cOutputMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param cSelectType
   */  
export interface ProcessingSelectAll_input{
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
      /**  (S)elect or (U)nselect all  */  
   cSelectType:string,
}

export interface ProcessingSelectAll_output{
parameters : {
      /**  output parameters  */  
   cOutputMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param cSelectType
   */  
export interface ProcessingSelectByDemand_input{
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
      /**  The Contract Number to process  */  
   iDemandContractNum:number,
      /**  The Demand Head identifier to process  */  
   iDemandHeadSeq:number,
      /**  (S)elect or (U)nselect  */  
   cSelectType:string,
}

export interface ProcessingSelectByDemand_output{
parameters : {
      /**  output parameters  */  
   cOutputMessage:string,
}
}

   /** Required : 
      @param ds
      @param ipGroupID
      @param cSelectType
   */  
export interface ProcessingSelectWorkList_input{
   ds:Erp_Tablesets_DemandMassInputsTableset[],
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
      /**  (S)elect or (U)nselect  */  
   cSelectType:string,
}

export interface ProcessingSelectWorkList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandMassInputsTableset,
   cOutputMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param iDemandContractNum
      @param iDemandHeadSeq
      @param cRejectType
   */  
export interface RejectAllForDemand_input{
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
      /**  The Contract Number to process  */  
   iDemandContractNum:number,
      /**  The Demand Head identifier to process  */  
   iDemandHeadSeq:number,
      /**  (R)eject or (U)nreject  */  
   cRejectType:string,
}

export interface RejectAllForDemand_output{
parameters : {
      /**  output parameters  */  
   cOutputMessage:string,
}
}

   /** Required : 
      @param ipGroupID
      @param cPartNum
      @param cRejectType
   */  
export interface RejectAllForPart_input{
      /**  Demand Mass Review Current Group.  */  
   ipGroupID:string,
      /**  The Part Number to process  */  
   cPartNum:string,
      /**  (R)eject or (U)nreject  */  
   cRejectType:string,
}

export interface RejectAllForPart_output{
parameters : {
      /**  output parameters  */  
   cOutputMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface UnmatchAll_input{
   ds:Erp_Tablesets_DemandMassReviewTableset[],
}

export interface UnmatchAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DemandMassReviewTableset,
   cOutputMessage:string,
}
}

