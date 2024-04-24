import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.WorkStationSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/$metadata", {
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
   Summary: Calls GetRows for the service
   Description: Get WorkStations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WorkStations
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WorkStationRow
   */  
export function get_WorkStations(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkStationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkStationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WorkStations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WorkStationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WorkStationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WorkStations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations", {
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
   Summary: Calls GetByID to retrieve the WorkStation item
   Description: Calls GetByID to retrieve the WorkStation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WorkStation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WorkStationRow
   */  
export function get_WorkStations_Company_WorkStationID(Company:string, WorkStationID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WorkStationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations(" + Company + "," + WorkStationID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_WorkStationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WorkStation for the service
   Description: Calls UpdateExt to update WorkStation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WorkStation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WorkStationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WorkStations_Company_WorkStationID(Company:string, WorkStationID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations(" + Company + "," + WorkStationID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete WorkStation item
   Description: Call UpdateExt to delete WorkStation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WorkStation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WorkStations_Company_WorkStationID(Company:string, WorkStationID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations(" + Company + "," + WorkStationID + ")", {
          method: 'delete',
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
   Summary: Calls GetByID for the service
   Description: Get Devices items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Devices1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DeviceRow
   */  
export function get_WorkStations_Company_WorkStationID_Devices(Company:string, WorkStationID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DeviceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations(" + Company + "," + WorkStationID + ")/Devices", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DeviceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the Device item
   Description: Calls GetByID to retrieve the Device item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Device1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      @param Type Desc: Type   Required: True   Allow empty value : True
      @param DefaultDevice Desc: DefaultDevice   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DeviceRow
   */  
export function get_WorkStations_Company_WorkStationID_Devices_Company_WorkStationID_Type_DefaultDevice(Company:string, WorkStationID:string, Type:string, DefaultDevice:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DeviceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations(" + Company + "," + WorkStationID + ")/Devices(" + Company + "," + WorkStationID + "," + Type + "," + DefaultDevice + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DeviceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get Devices items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Devices
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DeviceRow
   */  
export function get_Devices(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DeviceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/Devices", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DeviceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Devices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DeviceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DeviceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Devices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/Devices", {
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
   Summary: Calls GetByID to retrieve the Device item
   Description: Calls GetByID to retrieve the Device item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Device
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      @param Type Desc: Type   Required: True   Allow empty value : True
      @param DefaultDevice Desc: DefaultDevice   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DeviceRow
   */  
export function get_Devices_Company_WorkStationID_Type_DefaultDevice(Company:string, WorkStationID:string, Type:string, DefaultDevice:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DeviceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/Devices(" + Company + "," + WorkStationID + "," + Type + "," + DefaultDevice + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DeviceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Device for the service
   Description: Calls UpdateExt to update Device. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Device
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      @param Type Desc: Type   Required: True   Allow empty value : True
      @param DefaultDevice Desc: DefaultDevice   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DeviceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Devices_Company_WorkStationID_Type_DefaultDevice(Company:string, WorkStationID:string, Type:string, DefaultDevice:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/Devices(" + Company + "," + WorkStationID + "," + Type + "," + DefaultDevice + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete Device item
   Description: Call UpdateExt to delete Device item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Device
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WorkStationID Desc: WorkStationID   Required: True   Allow empty value : True
      @param Type Desc: Type   Required: True   Allow empty value : True
      @param DefaultDevice Desc: DefaultDevice   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Devices_Company_WorkStationID_Type_DefaultDevice(Company:string, WorkStationID:string, Type:string, DefaultDevice:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/Devices(" + Company + "," + WorkStationID + "," + Type + "," + DefaultDevice + ")", {
          method: 'delete',
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WorkstationListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkstationListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkstationListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseWorkStation:string, whereClauseDevice:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseWorkStation!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWorkStation=" + whereClauseWorkStation
   }
   if(typeof whereClauseDevice!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDevice=" + whereClauseDevice
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/GetRows" + params, {
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
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(workStationID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof workStationID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "workStationID=" + workStationID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/GetByID" + params, {
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
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/GetCodeDescList", {
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
   Summary: Invoke method CheckDeviceTypeCount
   Description: Deterimine if a default device has been defined
   OperationID: CheckDeviceTypeCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDeviceTypeCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDeviceTypeCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDeviceTypeCount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/CheckDeviceTypeCount", {
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
   Summary: Invoke method CheckForDefaultDeviceType
   Description: Deterimine if a default device has been defined
   OperationID: CheckForDefaultDeviceType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForDefaultDeviceType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDefaultDeviceType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckForDefaultDeviceType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/CheckForDefaultDeviceType", {
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
   Summary: Invoke method DuplicateStation
   Description: To create a new part by duplicating from another.
   OperationID: DuplicateStation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateStation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateStation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateStation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/DuplicateStation", {
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
   Summary: Invoke method GetNewWorkStation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWorkStation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWorkStation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWorkStation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWorkStation(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/GetNewWorkStation", {
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
   Summary: Invoke method GetNewDevice
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDevice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDevice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDevice_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewDevice(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/GetNewDevice", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/GetBySysRowID" + params, {
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
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/GetBySysRowIDs" + params, {
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
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DeviceRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DeviceRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkStationRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WorkStationRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkstationListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WorkstationListRow[],
}

export interface Erp_Tablesets_DeviceRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the WorkStations  */  
   "WorkStationID":string,
      /**  A Device Description that uniquely describes a device within a workstation  */  
   "Description":string,
      /**  Comport setting for scale interface  */  
   "Comport":number,
      /**  BaudRate setting for scale  */  
   "BaudRate":number,
      /**  DataBits setting for scales  */  
   "DataBits":number,
      /**  Parity setting for scales  */  
   "Parity":number,
      /**  StopBits setting for scales  */  
   "StopBits":number,
      /**  TimeOut setting for scales  */  
   "TimeOut":number,
      /**  InquireMsg for scales  */  
   "InquireMsg":string,
      /**  AppendCR to append carrage return to scale interface  */  
   "AppendCR":boolean,
      /**  PrinterID for printer  */  
   "PrinterID":string,
      /**  PrinterUseage - Use defined for this printer at a WorkStation. Valid values are Forms, Reports and Labels.  */  
   "PrinterUsage":string,
      /**  Device Type - valid values are Scale or Printer  */  
   "Type":string,
      /**  This checkbox will designate the device to use when there are multiple devices of the same type within a workstation.  */  
   "DefaultDevice":boolean,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   "DeviceUOM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  USBVendorID  */  
   "USBVendorID":string,
      /**  USBProductID  */  
   "USBProductID":string,
      /**  USBUOM  */  
   "USBUOM":string,
      /**  USBUsagePage  */  
   "USBUsagePage":number,
   "BitFlag":number,
   "SysPrinterDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_WorkStationRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the WorkStations  */  
   "WorkStationID":string,
      /**  Description of the station  */  
   "Description":string,
      /**  If yes, the pack station will automatically enter '1' for the quantity  */  
   "AutoQty":boolean,
      /**   Describes how the weight is getting inputed
W = Prompt for Weight, P = Get Weight from Part, S = Get Weight from Scale  */  
   "WeightType":string,
      /**  If yes then enable manifest fields for entry  */  
   "UseManifest":boolean,
      /**  Defines which warehouse is to be used as the Warehouse for this station.  This must be a valid record in the Warehouse master file. It can't be blank.  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location for this Packing Station.  Bin Number cannot be blank.  */  
   "BinNum":string,
      /**  URL for Pack Out manifest information  */  
   "WebServiceUrl":string,
      /**  Defines WorkStation Type valid values are "Pack" and "Other"  */  
   "Type":string,
      /**  Must contain the following values:    Carton,  Master Pack or  Both. If "Carton is selected, the weight is acquired for each carton and each carton is manifested separately.  If Master Pack is selected, the weight is acquired for the master pack, and only the master pack is manifested.  If Both selected, weight is acquired either at Pack or Master Pack  */  
   "WeightCaptPt":string,
      /**  Unit of Measure of the Weight Class that is used as a default for the Shipping Total Weight.  */  
   "TransWUM":string,
      /**   Unit of measure used to qualify the Lenth, Height, Width to be used in the manifest.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")
System will take the length, width and height and the UOM defined in the package and will convert it to the length UOM defined in the manifest settings.  */  
   "SizeUOM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Specify how long in seconds  the client will wait for a response from your Freight Service  */  
   "TimeOut":number,
      /**  Enable to Log Manifest Request and Response XML Messages to the file. Enabled to the System manager only  */  
   "LogManifestMsg":boolean,
   "WhseList":string,
   "EnableLogManifestMsg":boolean,
      /**  This flag is to show/hide Log Manufest and TimeOut fields based on Freight Service Integration that user selected in Company configuration  */  
   "DispLogManifest":boolean,
   "BitFlag":number,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_WorkstationListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of the WorkStations  */  
   "WorkStationID":string,
      /**  Description of the station  */  
   "Description":string,
      /**  If yes, the pack station will automatically enter '1' for the quantity  */  
   "AutoQty":boolean,
      /**   Describes how the weight is getting inputed
W = Prompt for Weight, P = Get Weight from Part, S = Get Weight from Scale  */  
   "WeightType":string,
      /**  If yes then enable manifest fields for entry  */  
   "UseManifest":boolean,
      /**  Defines which warehouse is to be used as the Warehouse for this station.  This must be a valid record in the Warehouse master file. It can't be blank.  */  
   "WarehouseCode":string,
      /**  Identifies the Bin location for this Packing Station.  Bin Number cannot be blank.  */  
   "BinNum":string,
      /**  URL for Pack Out manifest information  */  
   "WebServiceUrl":string,
      /**  Defines WorkStation Type valid values are "Pack" and "Other"  */  
   "Type":string,
      /**  Must contain the following values:    Carton,  Master Pack or  Both. If "Carton is selected, the weight is acquired for each carton and each carton is manifested separately.  If Master Pack is selected, the weight is acquired for the master pack, and only the master pack is manifested.  If Both selected, weight is acquired either at Pack or Master Pack  */  
   "WeightCaptPt":string,
      /**  Unit of Measure of the Weight Class that is used as a default for the Shipping Total Weight.  */  
   "TransWUM":string,
      /**   Unit of measure used to qualify the Lenth, Height, Width to be used in the manifest.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")
System will take the length, width and height and the UOM defined in the package and will convert it to the length UOM defined in the manifest settings.  */  
   "SizeUOM":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "WhseList":string,
      /**  Description.  */  
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipworkstationID
      @param ipdeviceType
      @param ds
   */  
export interface CheckDeviceTypeCount_input{
      /**  Workstation ID  */  
   ipworkstationID:string,
      /**  Scale or Printer  */  
   ipdeviceType:string,
   ds:Erp_Tablesets_WorkStationTableset[],
}

export interface CheckDeviceTypeCount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkStationTableset[],
   deviceWarning:string,
}
}

   /** Required : 
      @param workstationID
      @param deviceType
   */  
export interface CheckForDefaultDeviceType_input{
      /**  Workstation ID  */  
   workstationID:string,
      /**  Scale or Printer  */  
   deviceType:string,
}

export interface CheckForDefaultDeviceType_output{
}

   /** Required : 
      @param workStationID
   */  
export interface DeleteByID_input{
   workStationID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param sourceStationID
      @param targetStationID
   */  
export interface DuplicateStation_input{
      /**  Source Station ID  */  
   sourceStationID:string,
      /**  Target Station ID  */  
   targetStationID:string,
}

export interface DuplicateStation_output{
   returnObj:Erp_Tablesets_WorkStationTableset[],
}

export interface Erp_Tablesets_DeviceRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the WorkStations  */  
   WorkStationID:string,
      /**  A Device Description that uniquely describes a device within a workstation  */  
   Description:string,
      /**  Comport setting for scale interface  */  
   Comport:number,
      /**  BaudRate setting for scale  */  
   BaudRate:number,
      /**  DataBits setting for scales  */  
   DataBits:number,
      /**  Parity setting for scales  */  
   Parity:number,
      /**  StopBits setting for scales  */  
   StopBits:number,
      /**  TimeOut setting for scales  */  
   TimeOut:number,
      /**  InquireMsg for scales  */  
   InquireMsg:string,
      /**  AppendCR to append carrage return to scale interface  */  
   AppendCR:boolean,
      /**  PrinterID for printer  */  
   PrinterID:string,
      /**  PrinterUseage - Use defined for this printer at a WorkStation. Valid values are Forms, Reports and Labels.  */  
   PrinterUsage:string,
      /**  Device Type - valid values are Scale or Printer  */  
   Type:string,
      /**  This checkbox will designate the device to use when there are multiple devices of the same type within a workstation.  */  
   DefaultDevice:boolean,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   DeviceUOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  USBVendorID  */  
   USBVendorID:string,
      /**  USBProductID  */  
   USBProductID:string,
      /**  USBUOM  */  
   USBUOM:string,
      /**  USBUsagePage  */  
   USBUsagePage:number,
   BitFlag:number,
   SysPrinterDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtWorkStationTableset{
   WorkStation:Erp_Tablesets_WorkStationRow[],
   Device:Erp_Tablesets_DeviceRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WorkStationRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the WorkStations  */  
   WorkStationID:string,
      /**  Description of the station  */  
   Description:string,
      /**  If yes, the pack station will automatically enter '1' for the quantity  */  
   AutoQty:boolean,
      /**   Describes how the weight is getting inputed
W = Prompt for Weight, P = Get Weight from Part, S = Get Weight from Scale  */  
   WeightType:string,
      /**  If yes then enable manifest fields for entry  */  
   UseManifest:boolean,
      /**  Defines which warehouse is to be used as the Warehouse for this station.  This must be a valid record in the Warehouse master file. It can't be blank.  */  
   WarehouseCode:string,
      /**  Identifies the Bin location for this Packing Station.  Bin Number cannot be blank.  */  
   BinNum:string,
      /**  URL for Pack Out manifest information  */  
   WebServiceUrl:string,
      /**  Defines WorkStation Type valid values are "Pack" and "Other"  */  
   Type:string,
      /**  Must contain the following values:    Carton,  Master Pack or  Both. If "Carton is selected, the weight is acquired for each carton and each carton is manifested separately.  If Master Pack is selected, the weight is acquired for the master pack, and only the master pack is manifested.  If Both selected, weight is acquired either at Pack or Master Pack  */  
   WeightCaptPt:string,
      /**  Unit of Measure of the Weight Class that is used as a default for the Shipping Total Weight.  */  
   TransWUM:string,
      /**   Unit of measure used to qualify the Lenth, Height, Width to be used in the manifest.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")
System will take the length, width and height and the UOM defined in the package and will convert it to the length UOM defined in the manifest settings.  */  
   SizeUOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Specify how long in seconds  the client will wait for a response from your Freight Service  */  
   TimeOut:number,
      /**  Enable to Log Manifest Request and Response XML Messages to the file. Enabled to the System manager only  */  
   LogManifestMsg:boolean,
   WhseList:string,
   EnableLogManifestMsg:boolean,
      /**  This flag is to show/hide Log Manufest and TimeOut fields based on Freight Service Integration that user selected in Company configuration  */  
   DispLogManifest:boolean,
   BitFlag:number,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WorkStationTableset{
   WorkStation:Erp_Tablesets_WorkStationRow[],
   Device:Erp_Tablesets_DeviceRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WorkstationListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the WorkStations  */  
   WorkStationID:string,
      /**  Description of the station  */  
   Description:string,
      /**  If yes, the pack station will automatically enter '1' for the quantity  */  
   AutoQty:boolean,
      /**   Describes how the weight is getting inputed
W = Prompt for Weight, P = Get Weight from Part, S = Get Weight from Scale  */  
   WeightType:string,
      /**  If yes then enable manifest fields for entry  */  
   UseManifest:boolean,
      /**  Defines which warehouse is to be used as the Warehouse for this station.  This must be a valid record in the Warehouse master file. It can't be blank.  */  
   WarehouseCode:string,
      /**  Identifies the Bin location for this Packing Station.  Bin Number cannot be blank.  */  
   BinNum:string,
      /**  URL for Pack Out manifest information  */  
   WebServiceUrl:string,
      /**  Defines WorkStation Type valid values are "Pack" and "Other"  */  
   Type:string,
      /**  Must contain the following values:    Carton,  Master Pack or  Both. If "Carton is selected, the weight is acquired for each carton and each carton is manifested separately.  If Master Pack is selected, the weight is acquired for the master pack, and only the master pack is manifested.  If Both selected, weight is acquired either at Pack or Master Pack  */  
   WeightCaptPt:string,
      /**  Unit of Measure of the Weight Class that is used as a default for the Shipping Total Weight.  */  
   TransWUM:string,
      /**   Unit of measure used to qualify the Lenth, Height, Width to be used in the manifest.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")
System will take the length, width and height and the UOM defined in the package and will convert it to the length UOM defined in the manifest settings.  */  
   SizeUOM:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   WhseList:string,
      /**  Description.  */  
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WorkstationListTableset{
   WorkstationList:Erp_Tablesets_WorkstationListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param workStationID
   */  
export interface GetByID_input{
   workStationID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_WorkStationTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_WorkStationTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_WorkStationTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_WorkstationListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param workStationID
      @param type
   */  
export interface GetNewDevice_input{
   ds:Erp_Tablesets_WorkStationTableset[],
   workStationID:string,
   type:string,
}

export interface GetNewDevice_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkStationTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewWorkStation_input{
   ds:Erp_Tablesets_WorkStationTableset[],
}

export interface GetNewWorkStation_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkStationTableset[],
}
}

   /** Required : 
      @param whereClauseWorkStation
      @param whereClauseDevice
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseWorkStation:string,
   whereClauseDevice:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_WorkStationTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtWorkStationTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtWorkStationTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_WorkStationTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkStationTableset[],
}
}

