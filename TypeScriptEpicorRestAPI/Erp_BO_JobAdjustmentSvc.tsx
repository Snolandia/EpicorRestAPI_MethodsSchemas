import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.JobAdjustmentSvc
// Description: Job Adjustment Business Logic
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/$metadata", {
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
   Summary: Invoke method CalcUnitCost
   Description: This method should be run when any of the following fields change on the job material
adjustment sheet to recalcuate the extended unit cost;
ttJATrans.MtlUnitCost
ttJATrans.BurUnitCost
ttJATrans.LbrUnitCost
ttJATrans.SubUnitCost
ttJATrans.MtlBurUnitCost
   OperationID: CalcUnitCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalcUnitCost(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/CalcUnitCost", {
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
   Summary: Invoke method ChangeLaborAssemSeq
   Description: This method needs to be called when the Assembly changes on the material sheet.
   OperationID: ChangeLaborAssemSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborAssemSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborAssemSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborAssemSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeLaborAssemSeq", {
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
   Summary: Invoke method ChangeLaborComplete
   Description: This method should be invoked when the complete flag changes .
   OperationID: ChangeLaborComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborComplete(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeLaborComplete", {
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
   Summary: Invoke method ChangeLaborEmployeeNum
   Description: This method changes the name of the employee when the employee number changes.
   OperationID: ChangeLaborEmployeeNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborEmployeeNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborEmployeeNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborEmployeeNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeLaborEmployeeNum", {
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
   Summary: Invoke method ChangeLaborJobNum
   Description: This method validates the job number and resets the assembly and operation .
This validation is also performed when the transaction is committed.
   OperationID: ChangeLaborJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeLaborJobNum", {
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
   Summary: Invoke method ChangeLaborOprSeq
   Description: This method needs to be called when the operation on the Labor sheet changes.
It validates the sequences  and pulls in some defaults .
   OperationID: ChangeLaborOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborOprSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeLaborOprSeq", {
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
   Summary: Invoke method ChangeLaborType
   Description: Run this method when the labor type changes. Valid labor types are 's' setup or 'p'
production. This method will also set the ' complete ' flag appropriately.
   OperationID: ChangeLaborType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLaborType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeLaborType", {
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
   Summary: Invoke method ChangeMtlAssemSeq
   Description: This method needs to be called when the Assembly changes on the material sheet.
   OperationID: ChangeMtlAssemSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlAssemSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlAssemSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMtlAssemSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeMtlAssemSeq", {
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
   Summary: Invoke method ChangeMtlExtCost
   Description: This method should be run when the extended cost changes on the adjust material sheet.
   OperationID: ChangeMtlExtCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlExtCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlExtCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMtlExtCost(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeMtlExtCost", {
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
   Summary: Invoke method ChangeMtlJobMtl
   Description: This method should be invoked when the material changes. This method will find
the associated JobMtl record and reset the defaults.
   OperationID: ChangeMtlJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMtlJobMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeMtlJobMtl", {
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
   Summary: Invoke method ChangeMtlJobNum
   Description: This method should be invoked when the material changes. This method will find
the associated JobMtl record and reset the defaults.
   OperationID: ChangeMtlJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMtlJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeMtlJobNum", {
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
   Summary: Invoke method ChangeMtlTranQty
   Description: Run this method after the TranQty on the JobMaterial sheet is changed. This method
will recalculate totals for the new tran amount.
   OperationID: ChangeMtlTranQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMtlTranQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMtlTranQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMtlTranQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeMtlTranQty", {
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
   Summary: Invoke method ChangeSubAssemSeq
   Description: This method needs to be called when the Assembly changes on the subcontract sheet.
It clears out the JobSeq.
   OperationID: ChangeSubAssemSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubAssemSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubAssemSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSubAssemSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeSubAssemSeq", {
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
   Summary: Invoke method ChangeSubExtCost
   Description: Run this method after the ExtCost is changed on the Subcontract sheet.
This method will recalculate the total for SubUnitCost.
   OperationID: ChangeSubExtCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubExtCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubExtCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSubExtCost(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeSubExtCost", {
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
   Summary: Invoke method ChangeSubJobNum
   Description: This method validates the job number and resets the assembly and operation .
This validation is also performed when the transaction is committed.
   OperationID: ChangeSubJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSubJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeSubJobNum", {
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
   Summary: Invoke method ChangeSubOper
   Description: This method should be invoked when the Job Operation (JobSeq) on the SubContract
sheet changes. This method will find  .
   OperationID: ChangeSubOper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubOper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubOper_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSubOper(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeSubOper", {
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
   Summary: Invoke method ChangeSubTranQty
   Description: Run this method after the TranQty is changed on the Subcontract sheet. This method will recalculate totals
for the new Unit Cost.
   OperationID: ChangeSubTranQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubTranQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubTranQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSubTranQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeSubTranQty", {
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
   Summary: Invoke method ChangeSubUnitCost
   Description: Run this method after the SubUnitCost is changed on the Subcontract sheet.
This method will recalculate the ExtCost.
   OperationID: ChangeSubUnitCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubUnitCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubUnitCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSubUnitCost(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ChangeSubUnitCost", {
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
   Summary: Invoke method CommitLaborAdj
   Description: This method will validate and commit the Labor record .
   OperationID: CommitLaborAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitLaborAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitLaborAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CommitLaborAdj(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/CommitLaborAdj", {
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
   Summary: Invoke method CommitMaterialAdj
   Description: This method will validate and commit the Material adjustment record .
Before this is run, it is assumed that the ChangeMtlTranQty, ChangeMtlJobNum,
ChangeMtlJobMtl, ChangeMtlExtCost or CalcUnitCost were invoked on leave of a
the related field.
   OperationID: CommitMaterialAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitMaterialAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitMaterialAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CommitMaterialAdj(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/CommitMaterialAdj", {
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
   Summary: Invoke method CommitSubcontractAdj
   Description: This method should be run to commit the SubContract adjustment.
   OperationID: CommitSubcontractAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitSubcontractAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitSubcontractAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CommitSubcontractAdj(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/CommitSubcontractAdj", {
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
   Summary: Invoke method PreCommitMaterialAdj
   Description: This method will return a record in the LegalNumberGenerate datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreCommitMaterialAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCommitMaterialAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCommitMaterialAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreCommitMaterialAdj(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/PreCommitMaterialAdj", {
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
   Summary: Invoke method PreCommitSubcontractAdj
   Description: This method will return a record in the LegalNumberGenerate datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreCommitSubcontractAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCommitSubcontractAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCommitSubcontractAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreCommitSubcontractAdj(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/PreCommitSubcontractAdj", {
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
   Summary: Invoke method StartAdjustments
   Description: Use this method to start the Adjustment process .
   OperationID: StartAdjustments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartAdjustments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartAdjustments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartAdjustments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/StartAdjustments", {
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
   Summary: Invoke method StartLaborAdjustment
   Description: Use this method to start the Labor Adjustment process.
   OperationID: StartLaborAdjustment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartLaborAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartLaborAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartLaborAdjustment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/StartLaborAdjustment", {
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
   Summary: Invoke method StartMaterialAdjustment
   Description: This method starts the material adjustment process by creating a temp-table record with defaults.
Return added record
   OperationID: StartMaterialAdjustment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartMaterialAdjustment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartMaterialAdjustment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartMaterialAdjustment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/StartMaterialAdjustment", {
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
   Summary: Invoke method ReportPartQtyAllowed
   Description: Returns TRUE if Part Quantity Reporting is allowed for a given operation.
Notes: In order to be allowed the following conditions must be meet.
1. Must be final assembly (AssemblySeq = 0)
2. Must be the final operation.
3. Job must have more that one end part defined or has one or more Parts with PartPerOp > 1
/* NOTE: THIS IS A PUBLIC FUNCTION. HOWEVER, I DID NOT USE THE STANDARD TRY_PUBLIC/CATCH_PUBLIC.
THIS IS BECAUSE I WANT IT TO BE  CALLABLE BY THE CLIENT AND THE SERVER. IF A PUBLIC CALLS A PUBLIC
THE EXCEPTION MESSAGES WOULD GET CLEARED TOO EARLY.
*/
   OperationID: ReportPartQtyAllowed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReportPartQtyAllowed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportPartQtyAllowed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReportPartQtyAllowed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ReportPartQtyAllowed", {
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
   Summary: Invoke method ValidateChargeRateForTimeType
   Description: Validates if there is no valid Charge Rate according to selected Time Type.
This validation can also be found on BO/LaborApproval.
   OperationID: ValidateChargeRateForTimeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateChargeRateForTimeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateChargeRateForTimeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateChargeRateForTimeType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/ValidateChargeRateForTimeType", {
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
   Summary: Invoke method DefaultTimeTypCd
   Description: This method defaults dataset fields when the TimeTypCd field changes.
   OperationID: DefaultTimeTypCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultTimeTypCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultTimeTypCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultTimeTypCd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/DefaultTimeTypCd", {
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
   Summary: Invoke method DefaultRoleCd
   Description: This method defaults dataset fields when the RoleCd field changes.
   OperationID: DefaultRoleCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultRoleCd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/DefaultRoleCd", {
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
   Summary: Invoke method BuildJobOperPrjRoleList
   Description: This proc will return the where clause for the role code combo
Customers
   OperationID: BuildJobOperPrjRoleList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildJobOperPrjRoleList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildJobOperPrjRoleList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildJobOperPrjRoleList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/BuildJobOperPrjRoleList", {
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
   Summary: Invoke method GetAvailTranDocTypes
   Description: GetAvailTranDocTypes method.
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobAdjustmentSvc/GetAvailTranDocTypes", {
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



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipJobNum
      @param ipAssemblySeq
      @param ipOprSeq
      @param ipEmpID
   */  
export interface BuildJobOperPrjRoleList_input{
      /**  JobNum  */  
   ipJobNum:string,
      /**  AssemblySeq  */  
   ipAssemblySeq:number,
      /**  OprSeq  */  
   ipOprSeq:number,
      /**  EmpID  */  
   ipEmpID:string,
}

export interface BuildJobOperPrjRoleList_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   whereClause:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CalcUnitCost_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface CalcUnitCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param laborAssmSeq
      @param ds
   */  
export interface ChangeLaborAssemSeq_input{
      /**  LaborDtl.AssemblySeq  */  
   laborAssmSeq:number,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeLaborAssemSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param laborDtlComplete
      @param ds
   */  
export interface ChangeLaborComplete_input{
      /**  LaborDtl.complete  */  
   laborDtlComplete:boolean,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeLaborComplete_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param laborDtlEmployeeNum
      @param ds
   */  
export interface ChangeLaborEmployeeNum_input{
      /**  LaborDtl.EmployeeNum  */  
   laborDtlEmployeeNum:string,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeLaborEmployeeNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param laborDtlJobNum
      @param ds
   */  
export interface ChangeLaborJobNum_input{
      /**  LaborDtl.JobNum  */  
   laborDtlJobNum:string,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeLaborJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param laborDtlOprSeq
      @param ds
   */  
export interface ChangeLaborOprSeq_input{
      /**  LaborDtl.OprSeq  */  
   laborDtlOprSeq:number,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeLaborOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ttJALaborDtlLaborType
      @param ds
   */  
export interface ChangeLaborType_input{
      /**  ttJALaborDtl.LaborType  */  
   ttJALaborDtlLaborType:string,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeLaborType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param mtlAssmSeq
      @param ds
   */  
export interface ChangeMtlAssemSeq_input{
      /**  PartTran.AssemblySeq  */  
   mtlAssmSeq:number,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeMtlAssemSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ttJATransExtCost
      @param ds
   */  
export interface ChangeMtlExtCost_input{
      /**  PartTran.ExtCost  */  
   ttJATransExtCost:number,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeMtlExtCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param partTranJobSeq
      @param ds
   */  
export interface ChangeMtlJobMtl_input{
      /**  PartTran.JobSeq  */  
   partTranJobSeq:number,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeMtlJobMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param partTranJobNum
      @param ds
   */  
export interface ChangeMtlJobNum_input{
      /**  parttran.JobNum  */  
   partTranJobNum:string,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeMtlJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ttJATransTranQty
      @param ds
   */  
export interface ChangeMtlTranQty_input{
      /**  ttJATrans.TranQty  */  
   ttJATransTranQty:number,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeMtlTranQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ttJATransAssemblySeq
      @param ds
   */  
export interface ChangeSubAssemSeq_input{
      /**  PartTran.AssemblySeq  */  
   ttJATransAssemblySeq:number,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeSubAssemSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ttJATransExtCost
      @param ds
   */  
export interface ChangeSubExtCost_input{
      /**  parttran.ExtCost  */  
   ttJATransExtCost:number,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeSubExtCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ttJATransJobNum
      @param ds
   */  
export interface ChangeSubJobNum_input{
      /**  PartTran.JobNum  */  
   ttJATransJobNum:string,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeSubJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ttJATransJobSeq
      @param ds
   */  
export interface ChangeSubOper_input{
      /**  PartTran.JobSeq  */  
   ttJATransJobSeq:number,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeSubOper_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ttJATransTranQty
      @param ds
   */  
export interface ChangeSubTranQty_input{
      /**  PartTran.TranQty  */  
   ttJATransTranQty:number,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeSubTranQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ttJATransSubUnitCost
      @param ds
   */  
export interface ChangeSubUnitCost_input{
      /**  PartTran.SubUnitCost  */  
   ttJATransSubUnitCost:number,
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ChangeSubUnitCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CommitLaborAdj_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface CommitLaborAdj_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CommitMaterialAdj_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface CommitMaterialAdj_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
   legalNumberMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CommitSubcontractAdj_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface CommitSubcontractAdj_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
   legalNumberMessage:string,
}
}

   /** Required : 
      @param ds
      @param ipRoleCd
   */  
export interface DefaultRoleCd_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
      /**  Proposed RoleCd change  */  
   ipRoleCd:string,
}

export interface DefaultRoleCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ds
      @param ipTimeTypCd
   */  
export interface DefaultTimeTypCd_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
      /**  Proposed TimeTypCd change  */  
   ipTimeTypCd:string,
}

export interface DefaultTimeTypCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
   vMessage:string,
}
}

export interface Erp_Tablesets_JAAsmblyRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   HasLabor:boolean,
   HasMaterial:boolean,
   HasSubContract:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JAJobsRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   JobSeq:number,
   OperType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JALaborDtlRow{
   ClockInDate:string,
   LaborNote:string,
   AssemblySeq:number,
   OprSeq:number,
   QtyCompleted:number,
   ActProdHours:number,
   ActSetupHours:number,
   ActBurCost:number,
   ActLabCost:number,
   EmployeeNum:string,
   EmployeeName:string,
   LaborQty:number,
   LaborType:string,
   LaborHrs:number,
   LaborCost:number,
   BurdenHrs:number,
   BurdenCost:number,
   Complete:boolean,
   OpComplete:boolean,
   company:string,
   LaborHedSeq:number,
   LaborDtlSeq:number,
   OpCode:string,
   ResourceGrpID:string,
   JcDept:string,
   JobNum:string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
   EnableLaborQty:boolean,
   EnableScrapQty:boolean,
   EnableDiscrepQty:boolean,
      /**  Project Role Code  */  
   LaborRoleCd:string,
      /**  Field that indicates if field TimeTypCd should be disabled.  */  
   LaborDisTimeTypCd:boolean,
      /**  Field that indicates if field PrjRoleCd should be disabled.  */  
   LaborDisPrjRoleCd:boolean,
      /**  Time Type Code  */  
   LaborTimeTypeCd:string,
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JALaborPartRow{
   company:string,
   LaborHedSeq:number,
   LaborDtlSeq:number,
   JobNum:string,
   PartNum:string,
   PartQty:number,
   ReportedQty:number,
   PartDescription:string,
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JATransRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  A number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  Part Number that this transaction is for.  */  
   PartNum:string,
   IssuedQty:number,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   TranType:string,
      /**  date of transaction.  */  
   TranDate:string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   TranQty:number,
   TotalCost:number,
   ActUnitMtlCost:number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   UM:string,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
   ActUnitSubCost:number,
   ActUnitLbrCost:number,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
   ActUnitMtlBurCost:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
   ActUnitTotalCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   ExtCost:number,
      /**  Job Number that transaction is associated with.  */  
   JobNum:string,
      /**  Assembly Sequence #  */  
   AssemblySeq:number,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
   Reference:string,
   VenName:string,
   ActUnitBurCost:number,
   VendNum:number,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
   BaseIssuedQty:number,
   BaseTranQty:number,
      /**  Vendor purchase point ID. (see VendorNum)  */  
   PurPoint:string,
   BaseUOM:string,
      /**  Indicates whether the PartNum is flagged as serial tracked.  */  
   PartNumTrackSerialNum:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  */  
   VarTarget:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ExtMtlCost  */  
   ExtMtlCost:number,
      /**  ExtLbrCost  */  
   ExtLbrCost:number,
      /**  ExtBurCost  */  
   ExtBurCost:number,
      /**  ExtSubCost  */  
   ExtSubCost:number,
      /**  ExtMtlBurCost  */  
   ExtMtlBurCost:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JATransSubAsmblyRow{
   Company:string,
   TranDate:string,
   AssemblySeq:number,
   PartNum:string,
   PartDescription:string,
   IssuedQty:number,
   ExtMtlCost:number,
   ExtSubCost:number,
   ExtLbrCost:number,
   ExtMtlBurCost:number,
   TotalCost:number,
   ActUnitMtlCost:number,
   ActUnitSubCost:number,
   ActUnitLbrCost:number,
   ActUnitMtlBurCost:number,
   ActUnitTotalCost:number,
   TranQty:number,
   ExtCost:number,
   MtlUnitCost:number,
   SubUnitCost:number,
   MtlBurUnitCost:number,
   BurUnitCost:number,
   LbrUnitCost:number,
   Reference:string,
   VenName:string,
   SysDate:string,
   SysTime:number,
   TranNum:number,
   JobSeq:number,
   UM:string,
   ActUnitBurCost:number,
   MtlMtlUnitCost:number,
   ExtBurCost:number,
   VendNum:number,
   PurPoint:string,
   TranType:string,
   JobNum:string,
      /**  The flag to indicate if the Subcontract Operation is complete  */  
   OpComplete:boolean,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobAdjustmentTableset{
   JALaborDtl:Erp_Tablesets_JALaborDtlRow[],
   JALaborPart:Erp_Tablesets_JALaborPartRow[],
   JAAsmbly:Erp_Tablesets_JAAsmblyRow[],
   JAJobs:Erp_Tablesets_JAJobsRow[],
   JATrans:Erp_Tablesets_JATransRow[],
   JATransSubAsmbly:Erp_Tablesets_JATransSubAsmblyRow[],
   Jobs:Erp_Tablesets_JobsRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobsRow{
   Company:string,
   JobNum:string,
   SysRowID:string,
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

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   listAvailTranDocTypesMat:string,
   listAvailTranDocTypesSub:string,
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
      @param ds
   */  
export interface PreCommitMaterialAdj_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface PreCommitMaterialAdj_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface PreCommitSubcontractAdj_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface PreCommitSubcontractAdj_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ip_JobNum
      @param ip_AssemblySeq
      @param ip_OprSeq
   */  
export interface ReportPartQtyAllowed_input{
      /**  Job number  */  
   ip_JobNum:string,
      /**  Assembly Sequence number  */  
   ip_AssemblySeq:number,
      /**  Operation Sequence number  */  
   ip_OprSeq:number,
}

export interface ReportPartQtyAllowed_output{
      /**  true if the ReportPartQtyAllowed  */  
   returnObj:boolean,
}

   /** Required : 
      @param ds
   */  
export interface StartAdjustments_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface StartAdjustments_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ds
      @param jobNum
   */  
export interface StartLaborAdjustment_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
   jobNum:string,
}

export interface StartLaborAdjustment_output{
   returnObj:Erp_Tablesets_JALaborDtlRow[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ds
      @param inJobNum
   */  
export interface StartMaterialAdjustment_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
      /**  Job Number  */  
   inJobNum:string,
}

export interface StartMaterialAdjustment_output{
   returnObj:Erp_Tablesets_JATransRow[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateChargeRateForTimeType_input{
   ds:Erp_Tablesets_JobAdjustmentTableset[],
}

export interface ValidateChargeRateForTimeType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobAdjustmentTableset[],
   vMessage:string,
}
}

