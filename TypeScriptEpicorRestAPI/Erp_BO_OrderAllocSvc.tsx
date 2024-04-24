import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.OrderAllocSvc
// Description: Order Allocation data set
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/$metadata", {
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
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OrderAllocListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderAllocListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderAllocListRow)
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
   Summary: Invoke method AllocateByLotBin
   Description: Allocate sales demand records by choosing specific Lots and/or Bins
   OperationID: AllocateByLotBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AllocateByLotBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllocateByLotBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AllocateByLotBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderAllocListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/AllocateByLotBin", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderAllocListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AllocateBySerialNum
   Description: Allocate demand by choosing specific Serial Numbers
   OperationID: AllocateBySerialNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AllocateBySerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllocateBySerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AllocateBySerialNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/AllocateBySerialNum", {
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
   Summary: Invoke method AutoAllocation
   Description: Auto allocate demand
   OperationID: AutoAllocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoAllocation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoAllocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoAllocation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/AutoAllocation", {
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
   Summary: Invoke method AutoPick
   Description: Auto Pick demand
   OperationID: AutoPick
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoPick_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoPick_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoPick(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/AutoPick", {
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
   Summary: Invoke method AutoReserve
   Description: Auto reserve demand
   OperationID: AutoReserve
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoReserve_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoReserve_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoReserve(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/AutoReserve", {
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
   Summary: Invoke method AutoAllocateListOfJobs
   Description: Allocate a list of job materials
   OperationID: AutoAllocateListOfJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoAllocateListOfJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoAllocateListOfJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoAllocateListOfJobs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/AutoAllocateListOfJobs", {
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
   Summary: Invoke method AutoReserveListOfJobs
   Description: Reserve a list of job materials
   OperationID: AutoReserveListOfJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoReserveListOfJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoReserveListOfJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoReserveListOfJobs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/AutoReserveListOfJobs", {
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
   Summary: Invoke method AutoReserveJob
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipJobNum">Job Number</param><param name="ipAssemblySeq">AssemblySeq - can be zero</param><param name="ipCutoffDate">Cutoff Date - can be blank</param><returns>The AutoReserveJob data set</returns>
   OperationID: AutoReserveJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoReserveJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoReserveJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoReserveJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/AutoReserveJob", {
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
   Summary: Invoke method AutoUnreserveJob
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipJobNum">Job Number</param><param name="ipAssemblySeq">AssemblySeq - can be zero</param><param name="ipCutoffDate">Cutoff Date - can be blank</param>
   OperationID: AutoUnreserveJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoUnreserveJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoUnreserveJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoUnreserveJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/AutoUnreserveJob", {
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
   Summary: Invoke method ChangePartNum
   Description: Rebuild the AllocSupply list when the part number changes.  Prior to calling this
procedure, the RowMod field in all OrderAllocSupply records must be set to "U":U
because these records need to be cleared from the table before rebuilding the list.
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/ChangePartNum", {
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
   Summary: Invoke method ChangeStageBin
   Description: Validate the StageBin field
   OperationID: ChangeStageBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStageBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStageBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeStageBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/ChangeStageBin", {
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
   Summary: Invoke method ChangeStagingWarehouse
   Description: Default the staging bin based on the staging warehouse code passed in.
   OperationID: ChangeStagingWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStagingWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStagingWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeStagingWarehouse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/ChangeStagingWarehouse", {
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
   Summary: Invoke method CheckDates
   Description: Check Dates, return any warnings
   OperationID: CheckDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/CheckDates", {
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
   Summary: Invoke method CreateWave
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipWaveDesc">Wave Description</param><param name="ipDemandType">Demand Type - valid values are Order/Job/Transfer</param><param name="opWaveNum">New Wave Number</param>
   OperationID: CreateWave
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateWave_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateWave_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateWave(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/CreateWave", {
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
   Summary: Invoke method GetCalcPref
   Description: Purpose:
Parameters:  none
Notes:
<param name="opCalcFulfillOnSearch">Should calculations be executed after search? Yes/No</param>
   OperationID: GetCalcPref
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCalcPref_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCalcPref(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetCalcPref", {
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
   Summary: Invoke method GetFWBFulfillFromDemandWhseOnly
   Description: Purpose:
Parameters:  none
Notes:
<param name="opFWBFulfillFromDemandWhseOnly">FWB Fulfill From Demand Warehouse Only? Yes/No</param>
   OperationID: GetFWBFulfillFromDemandWhseOnly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFWBFulfillFromDemandWhseOnly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFWBFulfillFromDemandWhseOnly(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetFWBFulfillFromDemandWhseOnly", {
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
   Summary: Invoke method GetFWBLimitedRefresh
   Description: Purpose:
Parameters:  none
Notes:
<param name="opFWBLimitedRefresh">FWB Limited refresh? Yes/No</param>
   OperationID: GetFWBLimitedRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFWBLimitedRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFWBLimitedRefresh(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetFWBLimitedRefresh", {
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
   Summary: Invoke method GetList
   Description: Gets List of order records that can be selected for Order Allocation.
   OperationID: Get_GetList
      @param whereClause Desc: where condition without the where word   Required: True   Allow empty value : True
      @param pageSize Desc: # of records returned.  0 means all   Required: True
   Required: True
      @param NO_COMPANY Desc: NO_COMPANY   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, NO_COMPANY:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }
   if(typeof NO_COMPANY!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "NO_COMPANY=" + NO_COMPANY
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetList" + params, {
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
   Summary: Invoke method GetListAdvanced
   Description: Gets List of order records that can be selected for fulfillment.
   OperationID: GetListAdvanced
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListAdvanced_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListAdvanced_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListAdvanced(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetListAdvanced", {
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
   Summary: Invoke method callGetListBasicSearch
   Description: pre call to build params from "Basic" search screen
   OperationID: callGetListBasicSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/callGetListBasicSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/callGetListBasicSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_callGetListBasicSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/callGetListBasicSearch", {
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
   Summary: Invoke method GetListBasicSearch
   Description: Called from "Basic" search screen
   OperationID: GetListBasicSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListBasicSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListBasicSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListBasicSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetListBasicSearch", {
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
   Summary: Invoke method GetListFromSelectedKeys
   Description: This methods will return all of the OrderAlloc records which will be a subset
of the PartDtl records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetListFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListFromSelectedKeys(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetListFromSelectedKeys", {
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
   Summary: Invoke method GetListFWB
   Description: Gets List of order records that can be selected for Order Allocation.
            
GetListFWB is used by programs that want to filter GetList results using the Ready to Fulfill flag (example: Fulfillment Workbench)
GetList is available for programs that do not want to consider the Ready to Fulfill flag (example: PartTracker)
   OperationID: GetListFWB
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFWB_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFWB_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListFWB(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetListFWB", {
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
   Summary: Invoke method GetListAndOrderAllocationGetRows
   Description: Executes GetList using a whereClause passed by the caller
and uses that ds to call OrderAllocationGetRows, which refreshes rows data only for the selected list rows.
            
For BO calls such as the REST equivalent of the PartTracker retrieval of Allocation data
   OperationID: GetListAndOrderAllocationGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListAndOrderAllocationGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListAndOrderAllocationGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListAndOrderAllocationGetRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetListAndOrderAllocationGetRows", {
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
   Summary: Invoke method callGetListOfJobs
   Description: pre call to build List params from GetListOfJobs search.
   OperationID: callGetListOfJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/callGetListOfJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/callGetListOfJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_callGetListOfJobs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/callGetListOfJobs", {
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
   Summary: Invoke method GetListOfJobs
   Description: Gets List of Job records that can be selected for fulfillment.
   OperationID: GetListOfJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfJobs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetListOfJobs", {
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
   Summary: Invoke method callGetListOfOrders
   Description: pre call to build params from "GetListOfOrders" search
   OperationID: callGetListOfOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/callGetListOfOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/callGetListOfOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_callGetListOfOrders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/callGetListOfOrders", {
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
   Summary: Invoke method GetListOfOrders
   Description: Gets List of order records that can be selected for Order Allocation.
   OperationID: GetListOfOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfOrders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetListOfOrders", {
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
   Summary: Invoke method callGetListOfTransferOrders
   Description: pre call to build List params from GetListOfTransferOrders search.
   OperationID: callGetListOfTransferOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/callGetListOfTransferOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/callGetListOfTransferOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_callGetListOfTransferOrders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/callGetListOfTransferOrders", {
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
   Summary: Invoke method GetListOfTransferOrders
   Description: Gets List of Transfer Order records that can be selected for fulfillment.
   OperationID: GetListOfTransferOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfTransferOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfTransferOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfTransferOrders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetListOfTransferOrders", {
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
   Summary: Invoke method GetLotBinOnHand
   Description: Select OrderAlloc rows based on criteria.
   OperationID: GetLotBinOnHand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLotBinOnHand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLotBinOnHand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLotBinOnHand(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetLotBinOnHand", {
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
   Summary: Invoke method GetLotBinOnHandByWhseCode
   Description: Select OrderAlloc rows based on criteria for warehouse, pass a blank warehouse to include all warehouses.
   OperationID: GetLotBinOnHandByWhseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLotBinOnHandByWhseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLotBinOnHandByWhseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLotBinOnHandByWhseCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetLotBinOnHandByWhseCode", {
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
   Summary: Invoke method GetLotBinOnHandByWhseCodeZoneBinType
   Description: Select OrderAlloc rows based on criteria for warehouse, pass a blank warehouse to include all warehouses.
   OperationID: GetLotBinOnHandByWhseCodeZoneBinType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLotBinOnHandByWhseCodeZoneBinType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLotBinOnHandByWhseCodeZoneBinType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLotBinOnHandByWhseCodeZoneBinType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetLotBinOnHandByWhseCodeZoneBinType", {
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
   Summary: Invoke method GetOrderAllocFields
   Description: Returns a DataSet containing a list of the OrderAlloc fields for use in the Selection Filter in Fulfillment Workbench
   OperationID: GetOrderAllocFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderAllocFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderAllocFields(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetOrderAllocFields", {
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
   Summary: Invoke method GetRowsFromSelectedKeys
   Description: This methods will return all of the OrderAlloc records which will be a subset
of the PartDtl records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method.
   OperationID: GetRowsFromSelectedKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsFromSelectedKeys(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetRowsFromSelectedKeys", {
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
   Summary: Invoke method GetSerialNumOnHand
   Description: Select OrderAlloc rows based on criteria.
   OperationID: GetSerialNumOnHand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNumOnHand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumOnHand_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSerialNumOnHand(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetSerialNumOnHand", {
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
   Summary: Invoke method GetSerialNumOnHandByWhseCode
   Description: Select OrderAlloc rows based on criteria for warehouse, pass a blank warehouse to include all warehouses.
   OperationID: GetSerialNumOnHandByWhseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNumOnHandByWhseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumOnHandByWhseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSerialNumOnHandByWhseCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetSerialNumOnHandByWhseCode", {
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
   Summary: Invoke method GetSerialNumOnHandByWhseCodeZoneBinType
   Description: Select OrderAlloc rows based on criteria for warehouse, pass a blank warehouse to include all warehouses.
   OperationID: GetSerialNumOnHandByWhseCodeZoneBinType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNumOnHandByWhseCodeZoneBinType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumOnHandByWhseCodeZoneBinType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSerialNumOnHandByWhseCodeZoneBinType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetSerialNumOnHandByWhseCodeZoneBinType", {
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
   Summary: Invoke method GetSubmitOptionsList
   Description: Returns a delimited list of the pick options in code`Description format.  Each
code-Description entry is separated with character ~.
   OperationID: GetSubmitOptionsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSubmitOptionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSubmitOptionsList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetSubmitOptionsList", {
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
   Summary: Invoke method GetWarehouseInfo
   Description: This method returns the input warehouse and bin for a given job material record.
   OperationID: GetWarehouseInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWarehouseInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarehouseInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWarehouseInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetWarehouseInfo", {
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
   Summary: Invoke method GetWhseTeamUserList
   Description: Returns the list of all employees from Database Table WhseGroupEmp
   OperationID: GetWhseTeamUserList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWhseTeamUserList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWhseTeamUserList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWhseTeamUserList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetWhseTeamUserList", {
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
   Summary: Invoke method JobMtlUpdate
   Description: Update the JobMtl database table with changes saved to the OrderAlloc datatable.
   OperationID: JobMtlUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/JobMtlUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/JobMtlUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobMtlUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/JobMtlUpdate", {
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
   Summary: Invoke method MassAssign
   Description: Mass assign data in various columns as defined by user
   OperationID: MassAssign
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassAssign_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassAssign_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassAssign(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/MassAssign", {
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
   Summary: Invoke method MtlQueueUpdate
   Description: Material Queue Update
   OperationID: MtlQueueUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MtlQueueUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MtlQueueUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MtlQueueUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/MtlQueueUpdate", {
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
   Summary: Invoke method OnChangeWaveNum
   Description: OnChangeWaveNum
   OperationID: OnChangeWaveNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWaveNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWaveNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWaveNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/OnChangeWaveNum", {
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
   Summary: Invoke method OneDemandType
   Description: Only one Demand Type can be selected
   OperationID: OneDemandType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OneDemandType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OneDemandType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OneDemandType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/OneDemandType", {
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
   Summary: Invoke method OrderAllocationGetRows
   Description: Returns the full dataset.
   OperationID: OrderAllocationGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OrderAllocationGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OrderAllocationGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OrderAllocationGetRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/OrderAllocationGetRows", {
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
   Summary: Invoke method OrderAllocSupplyUpdate
   Description: Update the PartAlloc database table with changes saved to the OrderAllocSupply datatable.
   OperationID: OrderAllocSupplyUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OrderAllocSupplyUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OrderAllocSupplyUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OrderAllocSupplyUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/OrderAllocSupplyUpdate", {
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
   Summary: Invoke method OrderRelUpdate
   Description: Update the OrderRel database table with changes saved to the OrderAlloc datatable.
   OperationID: OrderRelUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OrderRelUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OrderRelUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OrderRelUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/OrderRelUpdate", {
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
   Summary: Invoke method Recalculate
   Description: Recalculate public method - called from Refresh Fulfillment button in Fulfillment Workbench
   OperationID: Recalculate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Recalculate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Recalculate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Recalculate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/Recalculate", {
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
   Summary: Invoke method RecalculateWithSorting
   Description: RecalculateWithSorting public method - called from Refresh Fulfillment button in Fulfillment Workbench and sorts records based on sort parameters
   OperationID: RecalculateWithSorting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecalculateWithSorting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecalculateWithSorting_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RecalculateWithSorting(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/RecalculateWithSorting", {
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
   Summary: Invoke method RefreshSelectedRows
   Description: Inputs a full dataset that has been filtered by the UI to only contain the
selected rows.  It uses the full dataset to build a list dataset to be used
to call OrderAllocationGetRows which returns those rows to be returned to the
UI to refresh only the selected rows.
   OperationID: RefreshSelectedRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshSelectedRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshSelectedRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshSelectedRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/RefreshSelectedRows", {
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
   Summary: Invoke method SelectForProcessing
   Description: Select OrderAlloc rows based on criteria.
   OperationID: SelectForProcessing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectForProcessing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectForProcessing_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectForProcessing(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/SelectForProcessing", {
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
   Summary: Invoke method SetCalcPref
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCalcFulfillOnSearch">Value to set UserComp.CalcFulfillOnSearch Yes/No</param>
   OperationID: SetCalcPref
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetCalcPref_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCalcPref_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetCalcPref(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/SetCalcPref", {
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
   Summary: Invoke method SetFWBFulfillFromDemandWhseOnly
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipFWBFulfillFromDemandWhseOnly">Value to set UserComp.FWBFulfillFromDemandWhseOnly Yes/No</param>
   OperationID: SetFWBFulfillFromDemandWhseOnly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetFWBFulfillFromDemandWhseOnly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFWBFulfillFromDemandWhseOnly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetFWBFulfillFromDemandWhseOnly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/SetFWBFulfillFromDemandWhseOnly", {
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
   Summary: Invoke method SetFWBLimitedRefresh
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipFWBLimitedRefresh">Value to set UserComp.FWBLimitedRefresh Yes/No</param>
   OperationID: SetFWBLimitedRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetFWBLimitedRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFWBLimitedRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetFWBLimitedRefresh(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/SetFWBLimitedRefresh", {
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
   Summary: Invoke method SubmitForPicking
   Description: Submit order releases for picking
   OperationID: SubmitForPicking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitForPicking_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitForPicking_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitForPicking(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/SubmitForPicking", {
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
   Summary: Invoke method TFOrdDtlUpdate
   Description: Update the TFOrdDtl database table with changes saved to the OrderAlloc datatable.
   OperationID: TFOrdDtlUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TFOrdDtlUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TFOrdDtlUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TFOrdDtlUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/TFOrdDtlUpdate", {
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
   Summary: Invoke method UnallocateAndReserve
   Description: Unallocate and Unreserve demand records
   OperationID: UnallocateAndReserve
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnallocateAndReserve_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnallocateAndReserve_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnallocateAndReserve(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/UnallocateAndReserve", {
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
   Summary: Invoke method UnallocateAndUnreserve
   Description: Unallocate and Unreserve sales demand records
   OperationID: UnallocateAndUnreserve
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnallocateAndUnreserve_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnallocateAndUnreserve_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnallocateAndUnreserve(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/UnallocateAndUnreserve", {
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
   Summary: Invoke method Unreserve
   Description: Unreserve demand
   OperationID: Unreserve
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Unreserve_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Unreserve_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Unreserve(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/Unreserve", {
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
   Summary: Invoke method GetSearchSortDefault
   Description: This methods will return all the Search Sort Defaults defined in the Plant Configuration
   OperationID: GetSearchSortDefault
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSearchSortDefault_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSearchSortDefault_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSearchSortDefault(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderAllocSvc/GetSearchSortDefault", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OrderAllocListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_OrderAllocListRow[],
}

export interface Erp_Tablesets_OrderAllocListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Sales Order Number  */  
   "OrderNum":number,
      /**  Sales order Line number that this order release is linked to.  */  
   "OrderLine":number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   "OrderRelNum":number,
   "OrderNumLineRel":string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   "ReqDate":string,
      /**  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  */  
   "PartNum":string,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   "WarehouseCode":string,
      /**  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   "SelectForPicking":boolean,
   "CustID":string,
   "CustName":string,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
   "JobNum":string,
   "AssemblySeq":number,
   "MtlSeq":number,
   "JobAssemblyMtl":string,
   "TFOrdNum":string,
   "TFOrdLine":number,
   "TFOrdNumTFOrdLine":string,
   "DemandType":string,
   "DemandTypeDesc":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DisplaySeq":number,
   "FromPlant":string,
   "JobType":string,
   "NeedByDate":string,
   "Plant":string,
   "PriorityCode":string,
   "RequestDate":string,
   "RequiredDate":string,
   "ToPlant":string,
      /**  This flag indicates if the sales order release is ready to be fulfilled.  */  
   "ReadyToFulfill":boolean,
   "PartDescription":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
      @param cIPWhseList
      @param cWhseType
   */  
export interface AllocateByLotBin_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  The list of warehouses  */  
   cIPWhseList:string,
      /**  All or primary warehouse only  */  
   cWhseType:string,
}

export interface AllocateByLotBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   cMessageText:string,
   lReleased:boolean,
}
}

   /** Required : 
      @param ds
      @param cIPWhseList
      @param cWhseType
   */  
export interface AllocateBySerialNum_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  The list of warehouses  */  
   cIPWhseList:string,
      /**  All or primary warehouse only  */  
   cWhseType:string,
}

export interface AllocateBySerialNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   cMessageText:string,
   lReleased:boolean,
}
}

   /** Required : 
      @param orderAllocListTS
      @param allocTemplateID
   */  
export interface AutoAllocateListOfJobs_input{
   orderAllocListTS:Erp_Tablesets_OrderAllocListTableset[],
      /**  Allocation Template ID to use when allocating  */  
   allocTemplateID:string,
}

export interface AutoAllocateListOfJobs_output{
parameters : {
      /**  output parameters  */  
   messageText:string,
}
}

   /** Required : 
      @param ds
      @param cIPWhseList
      @param cWhseType
   */  
export interface AutoAllocation_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  The list of warehouses  */  
   cIPWhseList:string,
      /**  All or primary warehouse only  */  
   cWhseType:string,
}

export interface AutoAllocation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   cMessageText:string,
   lReleased:boolean,
}
}

   /** Required : 
      @param ds
      @param cIPWhseList
   */  
export interface AutoPick_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  The list of warehouses  */  
   cIPWhseList:string,
}

export interface AutoPick_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   o_Success:boolean,
   cMessageText:string,
}
}

   /** Required : 
      @param ipJobNum
      @param ipAssemblySeq
      @param ipCutoffDate
   */  
export interface AutoReserveJob_input{
   ipJobNum:string,
   ipAssemblySeq:number,
   ipCutoffDate:string,
}

export interface AutoReserveJob_output{
   returnObj:Erp_Tablesets_AutoReserveJobTableset[],
}

   /** Required : 
      @param orderAllocListTS
   */  
export interface AutoReserveListOfJobs_input{
   orderAllocListTS:Erp_Tablesets_OrderAllocListTableset[],
}

export interface AutoReserveListOfJobs_output{
parameters : {
      /**  output parameters  */  
   messageText:string,
}
}

   /** Required : 
      @param ds
      @param cIPWhseList
      @param cWhseType
   */  
export interface AutoReserve_input{
   ds:Erp_Tablesets_SlimOrderAllocTableset[],
      /**  The list of warehouses  */  
   cIPWhseList:string,
      /**  All or primary warehouse only  */  
   cWhseType:string,
}

export interface AutoReserve_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SlimOrderAllocTableset[],
   cMessageText:string,
}
}

   /** Required : 
      @param ipJobNum
      @param ipAssemblySeq
      @param ipCutoffDate
   */  
export interface AutoUnreserveJob_input{
   ipJobNum:string,
   ipAssemblySeq:number,
   ipCutoffDate:string,
}

export interface AutoUnreserveJob_output{
}

   /** Required : 
      @param ds
      @param cPartNum
      @param iOrderNum
      @param iOrderLine
      @param iOrderRelNum
   */  
export interface ChangePartNum_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  The part number  */  
   cPartNum:string,
      /**  The order number  */  
   iOrderNum:number,
      /**  The order line  */  
   iOrderLine:number,
      /**  The order release number  */  
   iOrderRelNum:number,
}

export interface ChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
      @param proposedStageBin
   */  
export interface ChangeStageBin_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  The proposed bin  */  
   proposedStageBin:string,
}

export interface ChangeStageBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
      @param cProposedStageWhseCode
   */  
export interface ChangeStagingWarehouse_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  The proposed warehouse code  */  
   cProposedStageWhseCode:string,
}

export interface ChangeStagingWarehouse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface CheckDates_input{
   ds:Erp_Tablesets_SlimOrderAllocTableset[],
}

export interface CheckDates_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SlimOrderAllocTableset[],
   cMessageText:string,
}
}

   /** Required : 
      @param ipWaveDesc
      @param ipDemandType
   */  
export interface CreateWave_input{
   ipWaveDesc:string,
   ipDemandType:string,
}

export interface CreateWave_output{
parameters : {
      /**  output parameters  */  
   opWaveNum:number,
}
}

export interface Erp_Tablesets_AutoReserveJobRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   OurReqQty:number,
   IUM:string,
   ReservedQty:number,
   AllocatedQty:number,
   PickingQty:number,
   PickedQty:number,
   FulfilledQty:number,
   RemainingToReserve:number,
   PartWhseOnHandQty:number,
   UnreservedInventory:number,
   PartNum:string,
      /**  AttrClassID  */  
   AttrClassID:string,
      /**  The Full Description of the Attribute Set  */  
   AttributeSetDescription:string,
      /**  AttributeSetID  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute S  */  
   AttributeSetShortDescription:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AutoReserveJobTableset{
   AutoReserveJob:Erp_Tablesets_AutoReserveJobRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_OrderAllocListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   OrderRelNum:number,
   OrderNumLineRel:string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   ReqDate:string,
      /**  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  */  
   PartNum:string,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   WarehouseCode:string,
      /**  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
   CustID:string,
   CustName:string,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   JobAssemblyMtl:string,
   TFOrdNum:string,
   TFOrdLine:number,
   TFOrdNumTFOrdLine:string,
   DemandType:string,
   DemandTypeDesc:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DisplaySeq:number,
   FromPlant:string,
   JobType:string,
   NeedByDate:string,
   Plant:string,
   PriorityCode:string,
   RequestDate:string,
   RequiredDate:string,
   ToPlant:string,
      /**  This flag indicates if the sales order release is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
   PartDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderAllocListTableset{
   OrderAllocList:Erp_Tablesets_OrderAllocListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_OrderAllocRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   OrderRelNum:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   ReqDate:string,
      /**  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   OurReqQty:number,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  */  
   ShipViaCode:string,
      /**  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   OpenRelease:boolean,
      /**  Indicates if this release is  "FIRM". The opposite is an uncommitted release, that is when the customer gives releases that are just 'Best Guesses' of what they will require in the future, such as in blanket order situations. This type of  releases is no different to the system, except that the FirmRelease field will be printed on reports such as TimePhase requirements.  */  
   FirmRelease:boolean,
      /**   Indicates if this requirement or any part of it will be manufactured. Default the setting to "No" if valid Part and the Part.Type is "S" or "P".

Default the setting to "Yes" if the part is not found in Part master or the Part.Type = "J".  This flag also gets set if this release gets linked to a Job via Job Entry. There is an Index on this field so that we can display releases that need have a job assigned to them. This display is part of Job Entry.  */  
   Make:boolean,
      /**  The planned production quantity, using Our U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   OurJobQty:number,
      /**  Actual quantity, using our U/M, shipped from the Job.  Updated via the shipping process.  */  
   OurJobShippedQty:number,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.

When an OrderRel record is 'voided' any outstanding inventory allocations are relieved, OrderRel.OpenRelease is set to "no" and records are created/updated in the OrdJobMsg file for all the related  open OrderRel records if the OrderDtl that was tied to a Job to indicate that the line item was voided.  */  
   VoidRelease:boolean,
      /**  Quantity, using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   WarehouseCode:string,
      /**  Actual quantity, using our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  */  
   PartNum:string,
      /**  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  */  
   RevisionNum:string,
      /**  Indicates if this customer/shipto  is exempt from sales tax for this line item. If field is non-blank it is considered exempt. Defaults from the Customer/Shipto file.  This code is totally user definable and no validation is required. This field will be printed on the Tax report if this item is reportable .  */  
   TaxExempt:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Enter via a DDSL fill-in for contact name. Use OrderHed.ShpConNum when the OrderRel.ShipToNum = OrderHed.ShipToNum else use ShipTo.PrimScon as a default.  */  
   ShpConNum:number,
      /**  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  */  
   NeedByDate:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**  This field identifies Buy To Order releases.  */  
   BuyToOrder:boolean,
      /**  Purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   PONum:number,
      /**   Unit of Measure that qualifies the "our" quantity fields.
If a valid part then it is the Base Stocking UOM (Part.IUM).
A mirror image of OrderDtl.IUM. Not directly maintainable  */  
   IUM:string,
      /**   Selling Unit of measure. Qualifies the "Selling" quantity fields.
A mirror image of OrderDtl.SalesUM. Not directly maintainable.  */  
   SalesUM:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   DispOrderShippedQty:number,
   DispOrderRemainingQty:number,
   DispOurStockShippedQty:number,
   DispOurJobShippedQty:number,
   DispOrderReserved:number,
   DispOrderMfgReserved:number,
   DispOrderStockReserved:number,
   CustID:string,
   CustName:string,
   ShipToCity:string,
   ShipToState:string,
   ShipToZip:string,
   ShipToCountry:string,
   StagingWhseDescription:string,
   ErrorStatusDisplay:string,
   StageWhseCode:string,
   StageBin:string,
   EnableSelectForPicking:boolean,
   OrderNumLineRel:string,
   ShipViaCodeDescription:string,
   WarehouseCodeDescription:string,
   ShipToName:string,
   ShipToAddress1:string,
   ShipToAddress2:string,
   ShipToAddress3:string,
   SupplyPartNum:string,
   ReservePriorityCode:string,
   DoNotShipBeforeDate:string,
   CustGroupCode:string,
   KitParentPartNum:string,
   KitParentLine:number,
   SelectedForAction:boolean,
   ReservedQty:number,
   PickingQty:number,
   PickedQty:number,
   RemainingToReserve:number,
   UnitPrice:number,
   ExtPrice:number,
   UnreservedInventory:number,
   AvailablePercent:number,
   OrderRelShippedTotal:number,
   OrderedLessShipped:number,
   PartWhseOnHandQty:number,
   KitFulfillmentValuePct:number,
   KitFulfilledValuePct:number,
   PotentialReserveQty:number,
   FulfilledQtyPct:number,
   FulfillmentQtyPct:number,
   PartVolume:number,
   PartWeight:number,
   KitFlag:string,
   DoNotShipAfterDate:string,
   NeedsUpdate:boolean,
   KitShipComplete:boolean,
   KitQtyPer:number,
   AllocatedQty:number,
   ReservedQtyPct:number,
   AllocatedQtyPct:number,
   FulfilledQty:number,
   WaveNum:number,
   WaveDestBinNum:string,
   WavePickTicketPrinted:boolean,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackMultipleUOM:boolean,
   BTCustNum:number,
   BTCustID:string,
   ShipOrderComplete:boolean,
   CreditHold:boolean,
   BTCustName:string,
   AllocatedUM:string,
   ReservedUM:string,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   TFOrdNum:string,
   TFOrdLine:number,
   TFOrdNumTFOrdLine:string,
      /**  valid values: Order, Job or Transfer  */  
   DemandType:string,
      /**  OrderRel.OrderNum, JobMtl.JobNum or TFOrdHed.TFOrdNum  */  
   DemandKey1:string,
      /**  OrderRel.OrderLine, JobMtl.AssemblySeq or TFOrdDtl.TFOrdLine  */  
   DemandKey2:string,
      /**  OrderRel.OrderRelNum, JobMtl.MtlSeq  */  
   DemandKey3:string,
   JobAssemblyMtl:string,
   DemandTypeDesc:string,
      /**  The order in which the demand records should be Fulfilled.  */  
   FulfillmentSeq:number,
   CrossDockedQty:number,
   OrderFulfillmentPct:number,
   ReservePriorityOverride:number,
   CustCategory:string,
   CustTerritoryID:string,
   PartWeightUOM:string,
   NormalizedPartWeight:number,
   NormalizedPartWeightUOM:string,
   NormalizedPartVolume:number,
   NormalizedPartVolumeUOM:string,
   PartVolumeUOM:string,
   UnitPriceCurrencyCode:string,
   TotalValue:number,
   TotalVolume:number,
   TotalWeight:number,
   FulfillmentValue:number,
   FulfillmentValuePct:number,
   FulfilledValue:number,
   FulfilledValuePct:number,
   OrderProjectID:string,
   UDShortChar01:string,
   UDShortChar02:string,
   UDNumber01:number,
   UDNumber02:number,
   UDCheckbox01:boolean,
   UDCheckbox02:boolean,
   UDDate01:string,
   UDDate02:string,
   OrderCounterSale:boolean,
   DistributionType:string,
   WaveDesc:string,
   TFOrdToPlant:string,
   TFOrdToPlantName:string,
   TFOrdToPlantCity:string,
   TFOrdToPlantState:string,
   TFOrdToPlantZip:string,
   TFOrdToPlantCountry:string,
   TFOrdFromPlant:string,
   TFOrdFromWarehouseCode:string,
   PartProdCode:string,
   LineCount:number,
   OrderStatus:string,
   JobStatus:string,
   TFOrdStatus:string,
   CustRegionCode:string,
   JobStartDate:string,
   JobSchedCode:string,
   JobPartNum:string,
   ReleaseCount:number,
   ReleaseForPickingSeq:number,
   OrderHeld:boolean,
      /**  Used to indicate if the Job Material is backflush.  */  
   BackFlush:boolean,
   DisplaySeq:number,
   MtlQueueSeq:number,
   OrderPONum:string,
   OrderAllocSupplyCounter:number,
   KitOurReqQty:number,
   KitUnitPrice:number,
   KitExtPrice:number,
   KitPricing:string,
      /**  The description of the part.  */  
   PartDescription:string,
   RelatedToSchemaName:string,
   RelatedToTableName:string,
   RelatedToSysRowID:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
   PartAttrClassID:string,
      /**  The attribute set ID specified here is used to filter the part bin locations displayed when allocating by lot/bin.  */  
   FilterAttributeSetID:number,
      /**  The short description of the filter attribute set.  */  
   FilterAttributeSetShortDescription:string,
   TrackInventoryAttributes:boolean,
   TrackInventoryByRevision:boolean,
      /**  The quantity of a make direct sales order release that can be released for picking from manufacturing.  */  
   MtoAvailQty:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderAllocSupplyRow{
   Company:string,
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   PartNum:string,
   WarehouseCode:string,
   JobNum:string,
   OnHandQuantity:number,
   AllocatedQuantity:number,
   AvailableQuantity:number,
   ReservedQuantity:number,
   SupplySource:string,
   OrderNumLineRel:string,
   WIPQuantity:number,
   SupplyJobNum:string,
   DemandType:string,
   DemandKey1:string,
   DemandKey2:string,
   DemandKey3:string,
   AssemblySeq:number,
   MtlSeq:number,
   TFOrdNum:string,
   TFOrdLine:number,
   UOM:string,
   PickingQuantity:number,
   PickedQuantity:number,
   UnreservedQuantity:number,
   FulfilledQuantity:number,
   JobAssemblyMtl:string,
   TFOrdNumTFOrdLine:string,
   DisplaySeq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderAllocTableset{
   OrderAlloc:Erp_Tablesets_OrderAllocRow[],
   OrderAllocSupply:Erp_Tablesets_OrderAllocSupplyRow[],
   PartAlloc:Erp_Tablesets_PartAllocRow[],
   PartAllocLot:Erp_Tablesets_PartAllocLotRow[],
   PartAllocSerial:Erp_Tablesets_PartAllocSerialRow[],
   PartAllocTran:Erp_Tablesets_PartAllocTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartAllocLotRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part number that the allocation is for.  */  
   PartNum:string,
      /**  Warehouse that is quantity allocated is being supplied from.  */  
   WarehouseCode:string,
   BinNum:string,
      /**  Job that is supplying the allocated quantity  */  
   SupplyJobNum:string,
      /**  Order number of the order release that is allocated.  */  
   OrderNum:number,
      /**  Order line number of the order release that is allocated.  */  
   OrderLine:number,
      /**  Order release number of the order release that is allocated.  */  
   OrderRelNum:number,
      /**  Job number of the JobMtl/JobAsmbl that is allocated.  */  
   JobNum:string,
      /**  Assembly number of the JobMtl/JobAsmbl that is allocated.  */  
   AssemblySeq:number,
      /**  Material sequence number of the JobMtl that is allocated.  */  
   MtlSeq:number,
      /**  Transfer Order that is allocated.  */  
   TFOrdNum:string,
      /**  Transfer Order Line that is allocated.  */  
   TFOrdLine:number,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  */  
   DimCode:string,
      /**  Quantity that is "Allocated" for the demand (sales order, job or transfer order requirement).  This is a Hard Allocation.  Allocations for each type of demand are made via their corresponding Fulfillment Workbench.  */  
   AllocatedQty:number,
   Allocate:boolean,
   Unallocate:boolean,
   OnHandQty:number,
   AvailableQty:number,
   NewAllocatedQty:number,
   Batch:string,
   MfgBatch:string,
   MfgLot:string,
   HeatNum:string,
   FirmWare:string,
   BestBeforeDt:string,
   MfgDt:string,
   CureDt:string,
   ExpirationDate:string,
   PCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
   RelatedToSchemaName:string,
   RelatedToTableName:string,
   RelatedToSysRowID:string,
      /**  Attribute Class ID for the part  */  
   PartAttrClassID:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part number that the allocation is for.  */  
   PartNum:string,
      /**  Warehouse that is quantity allocated is being supplied from.  */  
   WarehouseCode:string,
      /**  The user defined bin number within the warehouse.  */  
   BinNum:string,
      /**  Job that is supplying the allocated quantity  */  
   SupplyJobNum:string,
      /**  Order number of the order release that is allocated.  */  
   OrderNum:number,
      /**  Order line number of the order release that is allocated.  */  
   OrderLine:number,
      /**  Order release number of the order release that is allocated.  */  
   OrderRelNum:number,
      /**  Job number of the JobMtl/JobAsmbl that is allocated.  */  
   JobNum:string,
      /**  Assembly number of the JobMtl/JobAsmbl that is allocated.  */  
   AssemblySeq:number,
      /**  Material sequence number of the JobMtl that is allocated.  */  
   MtlSeq:number,
      /**  Transfer Order that is allocated.  */  
   TFOrdNum:string,
      /**  Transfer Order Line that is allocated.  */  
   TFOrdLine:number,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  */  
   DimCode:string,
      /**   Quantity that is "Reserved" for the demand (sales order/job requirement).   Reservations for Orders are made via the Order Allocations program.
(Also see PartWhse.SalesReservedQty, JobHead.ReservedQty)  */  
   ReservedQty:number,
      /**  Quantity that is "Allocated" for the demand (sales order, job or transfer order requirement).  This is a Hard Allocation.  Allocations for each type of demand are made via their corresponding Fulfillment Workbench.  */  
   AllocatedQty:number,
      /**   Quantity that is in the picking process for a sales order.  Orders are selected for picking in the Order Allocations program.
Picking is another category of Hard Allocations which are excluded from available quantiity calculations"
(Also see PartWhse.SalesPickingQty)  */  
   PickingQty:number,
      /**   Quantity that has been picked a sales order.  Orders are picked when the material mover enters the  move transaction or if the staging whse/bin area is the same as the source whse/bin
Picked is another category of Hard Allocations which are excluded from available quantiity calculations"

(Also see PartWhse.SalesPickingQty)  */  
   PickedQty:number,
      /**  Valid values: Order, Job or Transfer.  */  
   DemandType:string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   DistributionType:string,
      /**  Creation Date  */  
   CreateDate:string,
      /**  Creation Time  */  
   CreateTime:number,
      /**  Wave Number.  */  
   WaveNum:number,
      /**  The user defined bin number within the warehouse to which the inventory in this Wave Allocation should be moved via a Bin-To-Bin move.  */  
   WaveDestBinNum:string,
      /**  When PartAlloc.WaveNum <> 0, a Wave Pick Ticket must be printed to move the inventory from the current bin to the destination bin.  This flag indicates if the Wave Pick Ticket has been printed.  */  
   WavePickTicketPrinted:boolean,
      /**  ID that uniquely Identifies a Zone within a warehouse.  */  
   ZoneID:string,
      /**  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   SearchSort:string,
      /**  Bin Type.  Valid values:  Standard, Managed or Both.  */  
   BinType:string,
      /**  The first option for the bin from which to select inventory within the warehouse.  */  
   BinNumFirstOption:string,
      /**  Warehouse Destination for the allocated qty.  */  
   WhseDestWarehouseCode:string,
      /**  Warehouse Group Identifier.  */  
   WhseGroupCode:string,
      /**  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   TransPriority:number,
      /**  True if Cross-Docking is enabled.  */  
   CrossDocking:boolean,
      /**  When Material Queue items are added, they should be automatically On Hold.  */  
   OnHold:boolean,
      /**  True if Multiple Parts Per Bin is allowed.  */  
   MultiplePartsPerBin:boolean,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   PackStation:string,
      /**  The user defined Production In bin number within the warehouse.  */  
   BinNumProductionIn:string,
      /**  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  */  
   ForwardStageGroup:string,
      /**  Hard Allocation  */  
   HardAllocation:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  Schema Name of the related row.  */  
   RelatedToSchemaName:string,
      /**  Table Name of the related row.  */  
   RelatedToTableName:string,
      /**  SysRowID of the related row.  */  
   RelatedToSysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   DemandKey1:string,
   DemandKey2:string,
   DemandKey3:string,
   OrderNumLineRel:string,
   CrossDockedQty:number,
   BitFlag:number,
   AssemblySeqDescription:string,
   AttributeSetIDDescription:string,
   AttributeSetIDShortDescription:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartNumTrackSerialNum:boolean,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumSalesUM:string,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocSerialRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part number that the allocation is for.  */  
   PartNum:string,
      /**  Warehouse that is quantity allocated is being supplied from.  */  
   WarehouseCode:string,
      /**  Bin number  */  
   BinNum:string,
      /**  Job that is supplying the allocated quantity  */  
   SupplyJobNum:string,
      /**  Order number of the order release that is allocated.  */  
   OrderNum:number,
      /**  Order line number of the order release that is allocated.  */  
   OrderLine:number,
      /**  Order release number of the order release that is allocated.  */  
   OrderRelNum:number,
      /**  Job number of the JobMtl/JobAsmbl that is allocated.  */  
   JobNum:string,
      /**  Assembly number of the JobMtl/JobAsmbl that is allocated.  */  
   AssemblySeq:number,
      /**  Material sequence number of the JobMtl that is allocated.  */  
   MtlSeq:number,
      /**  Transfer Order that is allocated.  */  
   TFOrdNum:string,
      /**  Transfer Order Line that is allocated.  */  
   TFOrdLine:number,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  */  
   DimCode:string,
      /**  The allocated Serial Number.  */  
   SerialNum:string,
      /**  Quantity that is "Allocated" for the demand (sales order, job or transfer order requirement).  This is a Hard Allocation.  Allocations for each type of demand are made via their corresponding Fulfillment Workbench.  */  
   AllocatedQty:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  Schema Name of the related row.  */  
   RelatedToSchemaName:string,
      /**  Table Name of the related row.  */  
   RelatedToTableName:string,
      /**  SysRowID of the related row.  */  
   RelatedToSysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   AvailableQty:number,
   NewAllocatedQty:number,
   OnHandQty:number,
   Unallocate:boolean,
   Allocate:boolean,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartAllocTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Allocation Transaction Identifier.  */  
   TranNum:number,
      /**  User ID  */  
   DcdUserID:string,
      /**  Part number that the allocation is for.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   RevisionNum:string,
      /**  Warehouse that is quantity allocated is being supplied from.  */  
   WarehouseCode:string,
      /**  The user defined bin number within the warehouse.  */  
   BinNum:string,
      /**  Job that is supplying the allocated quantity  */  
   SupplyJobNum:string,
      /**  Order number of the order release that is allocated.  */  
   OrderNum:number,
      /**  Order line number of the order release that is allocated.  */  
   OrderLine:number,
      /**  Order release number of the order release that is allocated.  */  
   OrderRelNum:number,
      /**  Job number of the JobMtl/JobAsmbl that is allocated.  */  
   JobNum:string,
      /**  Assembly number of the JobMtl/JobAsmbl that is allocated.  */  
   AssemblySeq:number,
      /**  Material sequence number of the JobMtl that is allocated.  */  
   MtlSeq:number,
      /**  Transfer Order that is allocated.  */  
   TFOrdNum:string,
      /**  Transfer Order Line that is allocated.  */  
   TFOrdLine:number,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  With 9.0 the use of this field has been changed. Dimensions have been replaced with a true Unit of Measure. This field, while retaining the same name, now actually is used to hold a UOMCode.  */  
   DimCode:string,
      /**  Quantity that is "Allocated" for the demand (sales order, job or transfer order requirement).  This is a Hard Allocation.  Allocations for each type of demand are made via their corresponding Fulfillment Workbench.  */  
   AllocatedQty:number,
      /**  Wave Number.  */  
   WaveNum:number,
      /**  Wave Description.  */  
   WaveDesc:string,
      /**  Part Allocation Template Identifier.  */  
   AllocTemplateID:string,
      /**  Allocation Type.  Valid values:  Order or Wave.  */  
   AllocType:string,
      /**  Part Allocation Demand Type.  Valid Values:  Order, Job, or Transfer.  */  
   DemandType:string,
      /**  ID that uniquely Identifies a Zone within a warehouse.  */  
   ZoneID:string,
      /**  Search Sort.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   SearchSort:string,
      /**  The first option for the bin from which to select inventory within the warehouse.  */  
   BinNumFirstOption:string,
      /**  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  */  
   DistributionType:string,
      /**  Warehouse Group Identifier.  */  
   WhseGroupCode:string,
      /**  Transaction Priority.  Valid values:  1,2,3,4,5,6,7,8,9,0.  One is the highest priority.  */  
   TransPriority:number,
      /**  True if Cross-Docking is enabled.  */  
   CrossDocking:boolean,
      /**  True if Multiple Parts Per Bin is allowed.  */  
   MultiplePartsPerBin:boolean,
      /**  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  */  
   PackStation:string,
      /**  The user defined Production In bin number within the warehouse.  */  
   BinNumProductionIn:string,
      /**  ID that uniquely Identifies a Forward Stage Group Bin Zone within a warehouse.  */  
   ForwardStageGroup:string,
      /**  Employee ID  */  
   EmpID:string,
      /**  Bin Type.  Valid values:  Standard, Managed or Both.  */  
   BinType:string,
      /**  When Material Queue items are added, they should be automatically On Hold.  */  
   OnHold:boolean,
      /**  Employee ID that should be assigned to process record from the queue.  */  
   AssignEmpID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Warehouse Destination for the allocated qty.  */  
   WhseDestWarehouseCode:string,
      /**  The allocated demand is ready to be Released to Picking.  */  
   ReleaseToPicking:boolean,
      /**  PCID  */  
   PCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   AddHoc:boolean,
   Replenishable:boolean,
   WaveRecordCountAfter:number,
   WaveRecordCountBefore:number,
   WarehouseCodeProductionIn:string,
      /**  Fulfill using demand warehouse only.  */  
   UseDemandWhseOnly:boolean,
      /**  Instructs the allocation logic to override the FWBUseDemandWhseOnly flag on the UserComp table when determining which warehouse(s) to allocate.  If true, the UseDemandWhseOnly flag on the PartAllocTran is used.  */  
   OverrideFWBUseDemandWhseOnly:boolean,
   BitFlag:number,
   AllocTempDescAllocTemplateDesc:string,
   BinDescDescription:string,
   BinProductionInDescDescription:string,
   ForwardStageZoneDescZoneDesc:string,
   WarehseDescDescription:string,
   WarehseDestDescDescription:string,
   WhseGrpDescWhseGroupDesc:string,
   WorkStationDescDescription:string,
   ZoneDescZoneDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SlimOrderAllocRow{
   AssemblySeq:number,
   Company:string,
   DemandType:string,
   DoNotShipAfterDate:string,
   DoNotShipBeforeDate:string,
   FulfillmentSeq:number,
   JobNum:string,
   MtlSeq:number,
   OrderLine:number,
   OrderNum:number,
   OrderRelNum:number,
   ReservePriorityOverride:number,
   SelectedForAction:boolean,
   TFOrdLine:number,
   TFOrdNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SlimOrderAllocTableset{
   SlimOrderAlloc:Erp_Tablesets_SlimOrderAllocRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WhseTeamEmpListRow{
   Company:string,
   WhseGroupCode:string,
   EmpID:string,
   EmpName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WhseTeamEmpListTableset{
   WhseTeamEmpList:Erp_Tablesets_WhseTeamEmpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetCalcPref_output{
parameters : {
      /**  output parameters  */  
   opCalcFulfillOnSearch:boolean,
}
}

export interface GetFWBFulfillFromDemandWhseOnly_output{
parameters : {
      /**  output parameters  */  
   opFWBFulfillFromDemandWhseOnly:boolean,
}
}

export interface GetFWBLimitedRefresh_output{
parameters : {
      /**  output parameters  */  
   opFWBLimitedRefresh:boolean,
}
}

   /** Required : 
      @param i_CustId
      @param i_GroupCode
      @param i_ReservePri
      @param i_FromDate
      @param i_ToDate
      @param i_StartOrder
      @param i_EndOrder
      @param i_PONum
      @param i_PartNum
      @param i_DoNotShipBefore
      @param i_ShipVia
      @param i_SortBy
      @param i_StartingAt
      @param i_Order
      @param i_Job
      @param i_Transfer
      @param pageSize
      @param absolutePage
   */  
export interface GetListAdvanced_input{
      /**  Customer ID associated with the release  */  
   i_CustId:string,
      /**  Customer Group Code associated with the release  */  
   i_GroupCode:string,
      /**  Reservation Priority Code associated with the release  */  
   i_ReservePri:string,
      /**  Earliest Ship Date  */  
   i_FromDate:string,
      /**  Latest Ship Date  */  
   i_ToDate:string,
      /**  Lowest Order Number  */  
   i_StartOrder:number,
      /**  Highest Order Number  */  
   i_EndOrder:number,
      /**  Customer PO Number associated with the release  */  
   i_PONum:string,
      /**  Part Number  */  
   i_PartNum:string,
      /**  Do Not Ship before date associated with the release  */  
   i_DoNotShipBefore:string,
      /**  Ship Via Code  */  
   i_ShipVia:string,
      /**  Sort By field  */  
   i_SortBy:string,
      /**  Starting At field  */  
   i_StartingAt:string,
      /**  Order filter  */  
   i_Order:boolean,
      /**  Job filter  */  
   i_Job:boolean,
      /**  Transfer filter  */  
   i_Transfer:boolean,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetListAdvanced_output{
   returnObj:Erp_Tablesets_OrderAllocListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListAndOrderAllocationGetRows_input{
      /**  where condition without the where word  */  
   whereClause:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetListAndOrderAllocationGetRows_output{
   returnObj:Erp_Tablesets_OrderAllocTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipPartFrom
      @param ipPartTo
      @param ipAttributeSetID
      @param ipWaveFrom
      @param ipWaveTo
      @param ipPlantFrom
      @param ipPlantTo
      @param ipWhseFrom
      @param ipWhseTo
      @param ipNeedByFrom
      @param ipNeedByTo
      @param ipOrderFrom
      @param ipOrderTo
      @param ipShipByFrom
      @param ipShipByTo
      @param ipDemandType
      @param ipSortBy
      @param pageSize
      @param absolutePage
   */  
export interface GetListBasicSearch_input{
      /**  From Part  */  
   ipPartFrom:string,
      /**  To Part  */  
   ipPartTo:string,
   ipAttributeSetID:number,
      /**  From Wave  */  
   ipWaveFrom:string,
      /**  To Wave  */  
   ipWaveTo:string,
      /**  From Plant  */  
   ipPlantFrom:string,
      /**  To Plant  */  
   ipPlantTo:string,
      /**  From Whse  */  
   ipWhseFrom:string,
      /**  To Whse  */  
   ipWhseTo:string,
      /**  From Need By Date  */  
   ipNeedByFrom:string,
      /**  To Need By Date  */  
   ipNeedByTo:string,
      /**  From Order Date  */  
   ipOrderFrom:string,
      /**  To Order Date  */  
   ipOrderTo:string,
      /**  To Ship By Date  */  
   ipShipByFrom:string,
      /**  From Ship By Date  */  
   ipShipByTo:string,
      /**  Demand Type  */  
   ipDemandType:string,
      /**  Sort By  */  
   ipSortBy:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetListBasicSearch_output{
   returnObj:Erp_Tablesets_OrderAllocListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListFWB_input{
      /**  where condition without the where word  */  
   whereClause:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetListFWB_output{
   returnObj:Erp_Tablesets_OrderAllocListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param pageSize
      @param absolutePage
   */  
export interface GetListFromSelectedKeys_input{
   ds:Erp_Tablesets_OrderAllocListTableset[],
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetListFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocListTableset[],
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePartDtl
      @param whereClauseJobMtl
      @param whereClauseJobHead
      @param whereClausePartAlloc
      @param whereClauseWaveOrder
      @param i_SortByOrder
      @param pageSize
      @param absolutePage
      @param NO_COMPANY
   */  
export interface GetListOfJobs_input{
      /**  PartDtl where condition without the where word  */  
   whereClausePartDtl:string,
      /**  JobMtl where condition without the where word  */  
   whereClauseJobMtl:string,
      /**  JobHead where condition without the where word  */  
   whereClauseJobHead:string,
      /**  PartAlloc where condition without the where word  */  
   whereClausePartAlloc:string,
      /**  WaveOrder where condition without the where word  */  
   whereClauseWaveOrder:string,
      /**  Sort condition WITH the by word  */  
   i_SortByOrder:string,
      /**  # of records returned. 0 means all  */  
   pageSize:number,
   absolutePage:number,
      /**  NO_COMPANY  */  
   NO_COMPANY:string,
}

export interface GetListOfJobs_output{
   returnObj:Erp_Tablesets_OrderAllocListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param waveWhereClause
      @param orderHedWhereClause
      @param orderDtlWhereClause
      @param orderRelWhereClause
      @param customerWhereClause
      @param partAllocWhereClause
      @param countryWhereClause
      @param shipToWhereClause
      @param creditHoldClause
      @param i_SortByOrder
      @param i_SortByWarehouse
      @param i_SortByAllocation
      @param pageSize
      @param absolutePage
      @param NO_COMPANY
   */  
export interface GetListOfOrders_input{
      /**  Order Head where clause  */  
   waveWhereClause:string,
      /**  Order Head where clause  */  
   orderHedWhereClause:string,
      /**  Order Dtl where clause  */  
   orderDtlWhereClause:string,
      /**  Order Release where clause  */  
   orderRelWhereClause:string,
      /**  Customer where clause  */  
   customerWhereClause:string,
      /**  PartAlloc where clause  */  
   partAllocWhereClause:string,
      /**  Country where clause  */  
   countryWhereClause:string,
      /**  ShipTo where clause  */  
   shipToWhereClause:string,
      /**  Credit Hold filter clause  */  
   creditHoldClause:string,
      /**  Sort By Order field  */  
   i_SortByOrder:string,
      /**  Sort By WarehouseCode  */  
   i_SortByWarehouse:string,
      /**  Sort By Allocated  */  
   i_SortByAllocation:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
      /**  NO_COMPANY  */  
   NO_COMPANY:string,
}

export interface GetListOfOrders_output{
   returnObj:Erp_Tablesets_OrderAllocListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePartDtl
      @param whereClauseTFOrdDtl
      @param whereClauseTFOrdHed
      @param whereClausePartAlloc
      @param whereClauseWaveOrder
      @param i_SortByOrder
      @param pageSize
      @param absolutePage
   */  
export interface GetListOfTransferOrders_input{
      /**  PartDtl where Clause  */  
   whereClausePartDtl:string,
      /**  TFOrdDtl where Clause  */  
   whereClauseTFOrdDtl:string,
      /**  TFOrdHed where Clause  */  
   whereClauseTFOrdHed:string,
      /**  PartAlloc where Clause  */  
   whereClausePartAlloc:string,
      /**  WaveOrder where Clause  */  
   whereClauseWaveOrder:string,
      /**  Sort By  */  
   i_SortByOrder:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetListOfTransferOrders_output{
   returnObj:Erp_Tablesets_OrderAllocListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
      @param NO_COMPANY
   */  
export interface GetList_input{
      /**  where condition without the where word  */  
   whereClause:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
      /**  NO_COMPANY  */  
   NO_COMPANY:string,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_OrderAllocListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param ipWarehouseCode
      @param ipWarehouseZone
      @param ipBinType
   */  
export interface GetLotBinOnHandByWhseCodeZoneBinType_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  Warehouse Code  */  
   ipWarehouseCode:string,
      /**  Warehouse Zone  */  
   ipWarehouseZone:string,
      /**  Bin Type  */  
   ipBinType:string,
}

export interface GetLotBinOnHandByWhseCodeZoneBinType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
      @param ipWarehouseCode
   */  
export interface GetLotBinOnHandByWhseCode_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  Warehouse Code  */  
   ipWarehouseCode:string,
}

export interface GetLotBinOnHandByWhseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetLotBinOnHand_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface GetLotBinOnHand_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

export interface GetOrderAllocFields_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param ds
      @param ipLastDisplaySeq
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsFromSelectedKeys_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  Last DisplaySeq value currently in the grid  */  
   ipLastDisplaySeq:number,
      /**  The page size, used only for UI adapter  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adapter  */  
   absolutePage:number,
}

export interface GetRowsFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   morePages:boolean,
}
}

   /** Required : 
      @param ipDemandType
   */  
export interface GetSearchSortDefault_input{
      /**  Demand Type - valid values are Order/Job/Transfer  */  
   ipDemandType:string,
}

export interface GetSearchSortDefault_output{
parameters : {
      /**  output parameters  */  
   opSearchSort:string,
}
}

   /** Required : 
      @param ds
      @param ipWarehouseCode
      @param ipWarehouseZone
      @param ipBinType
   */  
export interface GetSerialNumOnHandByWhseCodeZoneBinType_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  Warehouse Code  */  
   ipWarehouseCode:string,
      /**  Warehouse Zone  */  
   ipWarehouseZone:string,
      /**  Bin Type  */  
   ipBinType:string,
}

export interface GetSerialNumOnHandByWhseCodeZoneBinType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
      @param ipWarehouseCode
   */  
export interface GetSerialNumOnHandByWhseCode_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  Warehouse Code  */  
   ipWarehouseCode:string,
}

export interface GetSerialNumOnHandByWhseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetSerialNumOnHand_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface GetSerialNumOnHand_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

export interface GetSubmitOptionsList_output{
parameters : {
      /**  output parameters  */  
   cSubmitOptionsList:string,
}
}

   /** Required : 
      @param jobNum
      @param assemblySeq
      @param mtlSeq
   */  
export interface GetWarehouseInfo_input{
      /**  The job number of a job material record  */  
   jobNum:string,
      /**  The assembly sequence of a job material record  */  
   assemblySeq:number,
      /**  The material sequence of a job material record  */  
   mtlSeq:number,
}

export interface GetWarehouseInfo_output{
parameters : {
      /**  output parameters  */  
   inputWhse:string,
   inputBinNum:string,
}
}

   /** Required : 
      @param groupCode
   */  
export interface GetWhseTeamUserList_input{
      /**  Warehouse Group Code.  */  
   groupCode:string,
}

export interface GetWhseTeamUserList_output{
   returnObj:Erp_Tablesets_WhseTeamEmpListTableset[],
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
export interface JobMtlUpdate_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface JobMtlUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
      @param cStageWhseCode
      @param cStageBinNum
   */  
export interface MassAssign_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  Proposed staging warehouse code  */  
   cStageWhseCode:string,
      /**  Proposed staging bin number  */  
   cStageBinNum:string,
}

export interface MassAssign_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   cMessageText:string,
}
}

   /** Required : 
      @param iReleaseForPickingSeq
   */  
export interface MtlQueueUpdate_input{
      /**  This Release for Pickings Seq  */  
   iReleaseForPickingSeq:number,
}

export interface MtlQueueUpdate_output{
}

   /** Required : 
      @param newWaveNum
      @param ds
   */  
export interface OnChangeWaveNum_input{
      /**  Wave.WaveNum  */  
   newWaveNum:number,
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface OnChangeWaveNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OneDemandType_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface OneDemandType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   o_ErrorText:string,
   o_DemandType:string,
}
}

   /** Required : 
      @param ds
   */  
export interface OrderAllocSupplyUpdate_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface OrderAllocSupplyUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
      @param ipLastDisplaySeq
   */  
export interface OrderAllocationGetRows_input{
   ds:Erp_Tablesets_OrderAllocListTableset[],
      /**  Last DisplaySeq value currently in the grid  */  
   ipLastDisplaySeq:number,
}

export interface OrderAllocationGetRows_output{
   returnObj:Erp_Tablesets_OrderAllocTableset[],
}

   /** Required : 
      @param ds
   */  
export interface OrderRelUpdate_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface OrderRelUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
      @param sortColumn
      @param sortDirection
   */  
export interface RecalculateWithSorting_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  Column to sort  */  
   sortColumn:string,
      /**  Sort Direction asc/desc  */  
   sortDirection:string,
}

export interface RecalculateWithSorting_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Recalculate_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface Recalculate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface RefreshSelectedRows_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface RefreshSelectedRows_output{
   returnObj:Erp_Tablesets_OrderAllocTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
      @param cCountry
      @param cShipVia
      @param dEndDate
      @param cCustID
      @param cPartNum
      @param lAllDates
      @param dPctFillable
   */  
export interface SelectForProcessing_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  Country code  */  
   cCountry:string,
      /**  Ship Via code  */  
   cShipVia:string,
      /**  The end date  */  
   dEndDate:string,
      /**  The customer id  */  
   cCustID:string,
      /**  The part number  */  
   cPartNum:string,
      /**  Indicates if all dates should considered for the allocate process  */  
   lAllDates:boolean,
      /**  Percent Fillable  */  
   dPctFillable:number,
}

export interface SelectForProcessing_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   cMessageText:string,
}
}

   /** Required : 
      @param ipCalcFulfillOnSearch
   */  
export interface SetCalcPref_input{
   ipCalcFulfillOnSearch:boolean,
}

export interface SetCalcPref_output{
}

   /** Required : 
      @param ipFWBFulfillFromDemandWhseOnly
   */  
export interface SetFWBFulfillFromDemandWhseOnly_input{
   ipFWBFulfillFromDemandWhseOnly:boolean,
}

export interface SetFWBFulfillFromDemandWhseOnly_output{
}

   /** Required : 
      @param ipFWBLimitedRefresh
   */  
export interface SetFWBLimitedRefresh_input{
   ipFWBLimitedRefresh:boolean,
}

export interface SetFWBLimitedRefresh_output{
}

   /** Required : 
      @param ds
      @param iNumDays
      @param dNeedByDate
      @param lUseSpecifiedDate
   */  
export interface SubmitForPicking_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
      /**  Number of days prior to ship by date  */  
   iNumDays:number,
      /**  Specific need by date  */  
   dNeedByDate:string,
      /**  Use the specific date passed in  */  
   lUseSpecifiedDate:boolean,
}

export interface SubmitForPicking_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   cMessageText:string,
   iReleaseForPickingSeq:number,
   lReleased:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface TFOrdDtlUpdate_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface TFOrdDtlUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface UnallocateAndReserve_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface UnallocateAndReserve_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   cMessageText:string,
}
}

   /** Required : 
      @param ds
   */  
export interface UnallocateAndUnreserve_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface UnallocateAndUnreserve_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   cMessageText:string,
}
}

   /** Required : 
      @param ds
   */  
export interface Unreserve_input{
   ds:Erp_Tablesets_OrderAllocTableset[],
}

export interface Unreserve_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderAllocTableset[],
   cMessageText:string,
}
}

   /** Required : 
      @param ipPartFrom
      @param ipPartTo
      @param ipAttributeSetID
      @param ipWaveFrom
      @param ipWaveTo
      @param ipPlantFrom
      @param ipPlantTo
      @param ipWhseFrom
      @param ipWhseTo
      @param ipNeedByFrom
      @param ipNeedByTo
      @param ipOrderFrom
      @param ipOrderTo
      @param ipShipByFrom
      @param ipShipByTo
      @param ipDTOrders
      @param ipDTTransfer
      @param ipDTJob
      @param ipDTReserved
      @param ipDTAllocated
      @param ipDTPicking
      @param ipDTPicked
      @param ipSortBy
      @param pageSize
      @param absolutePage
   */  
export interface callGetListBasicSearch_input{
      /**  From Part  */  
   ipPartFrom:string,
      /**  To Part  */  
   ipPartTo:string,
   ipAttributeSetID:string,
      /**  From Wave  */  
   ipWaveFrom:string,
      /**  To Wave  */  
   ipWaveTo:string,
      /**  From Plant  */  
   ipPlantFrom:string,
      /**  To Plant  */  
   ipPlantTo:string,
      /**  From Whse  */  
   ipWhseFrom:string,
      /**  To Whse  */  
   ipWhseTo:string,
      /**  From Need By Date  */  
   ipNeedByFrom:string,
      /**  To Need By Date  */  
   ipNeedByTo:string,
      /**  From Order Date  */  
   ipOrderFrom:string,
      /**  To Order Date  */  
   ipOrderTo:string,
      /**  To Ship By Date  */  
   ipShipByFrom:string,
      /**  From Ship By Date  */  
   ipShipByTo:string,
      /**  Sales Orders selected value  */  
   ipDTOrders:string,
      /**  Transfer Orders selected value  */  
   ipDTTransfer:string,
      /**  Jobs selected value  */  
   ipDTJob:string,
      /**  Reserved selected value  */  
   ipDTReserved:string,
      /**  Allocated selected value  */  
   ipDTAllocated:string,
      /**  InPicking selected value  */  
   ipDTPicking:string,
      /**  Picked selected value  */  
   ipDTPicked:string,
      /**  Sort By  */  
   ipSortBy:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface callGetListBasicSearch_output{
   returnObj:Erp_Tablesets_OrderAllocListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipWaveFrom
      @param ipWaveTo
      @param ipJobNumFrom
      @param ipJobNumTo
      @param ipJobTypeFrom
      @param ipJobTypeTo
      @param ipWhseFrom
      @param ipWhseTo
      @param ipRequestedFrom
      @param ipRequestedTo
      @param ipRequiredFrom
      @param ipRequiredTo
      @param ipScheduledFrom
      @param ipScheduledTo
      @param ipSchedCodeFrom
      @param ipSchedCodeTo
      @param ipTeamFrom
      @param ipTeamTo
      @param ipPlannerFrom
      @param ipPlannerTo
      @param ipGroupFrom
      @param ipGroupTo
      @param ipProjIDFrom
      @param ipProjIDTo
      @param ipCustomerIDFrom
      @param ipCustomerIDTo
      @param ipPartFrom
      @param ipPartTo
      @param ipAttributeSetID
      @param ipReserved
      @param ipAllocated
      @param ipPicking
      @param ipPicked
      @param ipEngineered
      @param ipReleased
      @param ipComplete
      @param ipSortJobNum
      @param ipSortReqDate
      @param ipSortJobType
      @param ipSortPlant
      @param pageSize
      @param absolutePage
   */  
export interface callGetListOfJobs_input{
   ipWaveFrom:string,
   ipWaveTo:string,
   ipJobNumFrom:string,
   ipJobNumTo:string,
   ipJobTypeFrom:string,
   ipJobTypeTo:string,
   ipWhseFrom:string,
   ipWhseTo:string,
   ipRequestedFrom:string,
   ipRequestedTo:string,
   ipRequiredFrom:string,
   ipRequiredTo:string,
   ipScheduledFrom:string,
   ipScheduledTo:string,
   ipSchedCodeFrom:string,
   ipSchedCodeTo:string,
   ipTeamFrom:string,
   ipTeamTo:string,
   ipPlannerFrom:string,
   ipPlannerTo:string,
   ipGroupFrom:string,
   ipGroupTo:string,
   ipProjIDFrom:string,
   ipProjIDTo:string,
   ipCustomerIDFrom:string,
   ipCustomerIDTo:string,
   ipPartFrom:string,
   ipPartTo:string,
   ipAttributeSetID:string,
   ipReserved:string,
   ipAllocated:string,
   ipPicking:string,
   ipPicked:string,
   ipEngineered:string,
   ipReleased:string,
   ipComplete:string,
   ipSortJobNum:string,
   ipSortReqDate:string,
   ipSortJobType:string,
   ipSortPlant:string,
   pageSize:number,
   absolutePage:number,
}

export interface callGetListOfJobs_output{
   returnObj:Erp_Tablesets_OrderAllocListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipWaveFrom
      @param ipWaveTo
      @param ipOrderNumFrom
      @param ipOrderNumTo
      @param ipPriCodeFrom
      @param ipPriCodeTo
      @param ipWhseFrom
      @param ipWhseTo
      @param ipNeedByFrom
      @param ipNeedByTo
      @param ipOrderFrom
      @param ipOrderTo
      @param ipShipByFrom
      @param ipShipByTo
      @param ipCusGroupFrom
      @param ipCusGroupTo
      @param ipPartFrom
      @param ipPartTo
      @param ipAttributeSetID
      @param ipShipViaFrom
      @param ipShipViaTo
      @param ipShipToFrom
      @param ipShipToTo
      @param ipShipCityFrom
      @param ipShipCityTo
      @param ipShipStateFrom
      @param ipShipStateTo
      @param ipZipFrom
      @param ipZipTo
      @param ipShipCountryFrom
      @param ipShipCountryTo
      @param ipSoldToFrom
      @param ipSoldToTo
      @param ipCustPOFrom
      @param ipCustPOTo
      @param ipProjIDFrom
      @param ipProjIDTo
      @param ipReserved
      @param ipAllocated
      @param ipPicking
      @param ipPicked
      @param ipShipComp
      @param ipCreditHold
      @param ipUserHold
      @param ipCountSales
      @param ipSortOrder
      @param ipSortShipDate
      @param ipSortWhse
      @param ipSortAlloc
      @param pageSize
      @param absolutePage
   */  
export interface callGetListOfOrders_input{
   ipWaveFrom:string,
   ipWaveTo:string,
   ipOrderNumFrom:string,
   ipOrderNumTo:string,
   ipPriCodeFrom:string,
   ipPriCodeTo:string,
   ipWhseFrom:string,
   ipWhseTo:string,
   ipNeedByFrom:string,
   ipNeedByTo:string,
   ipOrderFrom:string,
   ipOrderTo:string,
   ipShipByFrom:string,
   ipShipByTo:string,
   ipCusGroupFrom:string,
   ipCusGroupTo:string,
   ipPartFrom:string,
   ipPartTo:string,
   ipAttributeSetID:string,
   ipShipViaFrom:string,
   ipShipViaTo:string,
   ipShipToFrom:string,
   ipShipToTo:string,
   ipShipCityFrom:string,
   ipShipCityTo:string,
   ipShipStateFrom:string,
   ipShipStateTo:string,
   ipZipFrom:string,
   ipZipTo:string,
   ipShipCountryFrom:number,
   ipShipCountryTo:number,
   ipSoldToFrom:string,
   ipSoldToTo:string,
   ipCustPOFrom:string,
   ipCustPOTo:string,
   ipProjIDFrom:string,
   ipProjIDTo:string,
   ipReserved:string,
   ipAllocated:string,
   ipPicking:string,
   ipPicked:string,
   ipShipComp:string,
   ipCreditHold:string,
   ipUserHold:string,
   ipCountSales:string,
   ipSortOrder:string,
   ipSortShipDate:string,
   ipSortWhse:string,
   ipSortAlloc:string,
   pageSize:number,
   absolutePage:number,
}

export interface callGetListOfOrders_output{
   returnObj:Erp_Tablesets_OrderAllocListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipWaveFrom
      @param ipWaveTo
      @param ipTransferFrom
      @param ipTransferTo
      @param ipLineStatus
      @param ipLineOpen
      @param ipPlantFrom
      @param ipPlantTo
      @param ipWhseFrom
      @param ipWhseTo
      @param ipTransOrderFrom
      @param ipTransOrderTo
      @param ipNeedFrom
      @param ipNeedTo
      @param ipShipFrom
      @param ipShipTo
      @param ipPartFrom
      @param ipPartTo
      @param ipAttributeSetID
      @param ipShipViaFrom
      @param ipShipViaTo
      @param ipReserved
      @param ipAllocated
      @param ipPicking
      @param ipPicked
      @param ipSortOrder
      @param ipShipBy
      @param ipToPlant
      @param pageSize
      @param absolutePage
   */  
export interface callGetListOfTransferOrders_input{
   ipWaveFrom:string,
   ipWaveTo:string,
   ipTransferFrom:string,
   ipTransferTo:string,
   ipLineStatus:string,
   ipLineOpen:string,
   ipPlantFrom:string,
   ipPlantTo:string,
   ipWhseFrom:string,
   ipWhseTo:string,
   ipTransOrderFrom:string,
   ipTransOrderTo:string,
   ipNeedFrom:string,
   ipNeedTo:string,
   ipShipFrom:string,
   ipShipTo:string,
   ipPartFrom:string,
   ipPartTo:string,
   ipAttributeSetID:string,
   ipShipViaFrom:string,
   ipShipViaTo:string,
   ipReserved:string,
   ipAllocated:string,
   ipPicking:string,
   ipPicked:string,
   ipSortOrder:string,
   ipShipBy:string,
   ipToPlant:string,
   pageSize:number,
   absolutePage:number,
}

export interface callGetListOfTransferOrders_output{
   returnObj:Erp_Tablesets_OrderAllocListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

