import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.DynamicReportSvc
// Description: The BAQ Report service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/$metadata", {
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
   Description: Get DynamicReports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynamicReports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQReportRow
   */  
export function get_DynamicReports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynamicReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DynamicReports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports", {
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
   Summary: Calls GetByID to retrieve the DynamicReport item
   Description: Calls GetByID to retrieve the DynamicReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynamicReport
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQReportRow
   */  
export function get_DynamicReports_BAQRptID(BAQRptID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DynamicReport for the service
   Description: Calls UpdateExt to update DynamicReport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynamicReport
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DynamicReports_BAQRptID(BAQRptID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")", {
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
   Summary: Call UpdateExt to delete DynamicReport item
   Description: Call UpdateExt to delete DynamicReport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynamicReport
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DynamicReports_BAQRptID(BAQRptID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")", {
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
   Description: Get BAQRptOptionFlds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQRptOptionFlds1
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptOptionFldRow
   */  
export function get_DynamicReports_BAQRptID_BAQRptOptionFlds(BAQRptID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptOptionFldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptOptionFlds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptOptionFldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQRptOptionFld item
   Description: Calls GetByID to retrieve the BAQRptOptionFld item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptOptionFld1
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptOptionFldRow
   */  
export function get_DynamicReports_BAQRptID_BAQRptOptionFlds_BAQRptID_Seq(BAQRptID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQRptOptionFldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptOptionFlds(" + BAQRptID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQRptOptionFldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BAQRptFilters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQRptFilters1
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptFilterRow
   */  
export function get_DynamicReports_BAQRptID_BAQRptFilters(BAQRptID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptFilters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQRptFilter item
   Description: Calls GetByID to retrieve the BAQRptFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptFilter1
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptFilterRow
   */  
export function get_DynamicReports_BAQRptID_BAQRptFilters_BAQRptID_Seq(BAQRptID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQRptFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptFilters(" + BAQRptID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQRptFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BAQRptSorts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQRptSorts1
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptSortRow
   */  
export function get_DynamicReports_BAQRptID_BAQRptSorts(BAQRptID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptSorts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQRptSort item
   Description: Calls GetByID to retrieve the BAQRptSort item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptSort1
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param SortID Desc: SortID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptSortRow
   */  
export function get_DynamicReports_BAQRptID_BAQRptSorts_BAQRptID_SortID(BAQRptID:string, SortID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQRptSortRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DynamicReports(" + BAQRptID + ")/BAQRptSorts(" + BAQRptID + "," + SortID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQRptSortRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BAQRptOptionFlds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQRptOptionFlds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptOptionFldRow
   */  
export function get_BAQRptOptionFlds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptOptionFldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptOptionFlds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptOptionFldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQRptOptionFlds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQRptOptionFldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQRptOptionFldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQRptOptionFlds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptOptionFlds", {
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
   Summary: Calls GetByID to retrieve the BAQRptOptionFld item
   Description: Calls GetByID to retrieve the BAQRptOptionFld item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptOptionFld
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptOptionFldRow
   */  
export function get_BAQRptOptionFlds_BAQRptID_Seq(BAQRptID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQRptOptionFldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptOptionFlds(" + BAQRptID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQRptOptionFldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BAQRptOptionFld for the service
   Description: Calls UpdateExt to update BAQRptOptionFld. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQRptOptionFld
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQRptOptionFldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BAQRptOptionFlds_BAQRptID_Seq(BAQRptID:string, Seq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptOptionFlds(" + BAQRptID + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete BAQRptOptionFld item
   Description: Call UpdateExt to delete BAQRptOptionFld item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQRptOptionFld
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BAQRptOptionFlds_BAQRptID_Seq(BAQRptID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptOptionFlds(" + BAQRptID + "," + Seq + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get BAQRptFilters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQRptFilters
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptFilterRow
   */  
export function get_BAQRptFilters(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptFilters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQRptFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQRptFilterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQRptFilterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQRptFilters(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptFilters", {
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
   Summary: Calls GetByID to retrieve the BAQRptFilter item
   Description: Calls GetByID to retrieve the BAQRptFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptFilter
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptFilterRow
   */  
export function get_BAQRptFilters_BAQRptID_Seq(BAQRptID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQRptFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptFilters(" + BAQRptID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQRptFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BAQRptFilter for the service
   Description: Calls UpdateExt to update BAQRptFilter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQRptFilter
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQRptFilterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BAQRptFilters_BAQRptID_Seq(BAQRptID:string, Seq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptFilters(" + BAQRptID + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete BAQRptFilter item
   Description: Call UpdateExt to delete BAQRptFilter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQRptFilter
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BAQRptFilters_BAQRptID_Seq(BAQRptID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptFilters(" + BAQRptID + "," + Seq + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get BAQRptSorts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQRptSorts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptSortRow
   */  
export function get_BAQRptSorts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQRptSorts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQRptSortRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQRptSortRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQRptSorts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts", {
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
   Summary: Calls GetByID to retrieve the BAQRptSort item
   Description: Calls GetByID to retrieve the BAQRptSort item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptSort
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param SortID Desc: SortID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptSortRow
   */  
export function get_BAQRptSorts_BAQRptID_SortID(BAQRptID:string, SortID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQRptSortRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts(" + BAQRptID + "," + SortID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQRptSortRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BAQRptSort for the service
   Description: Calls UpdateExt to update BAQRptSort. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQRptSort
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param SortID Desc: SortID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQRptSortRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BAQRptSorts_BAQRptID_SortID(BAQRptID:string, SortID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts(" + BAQRptID + "," + SortID + ")", {
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
   Summary: Call UpdateExt to delete BAQRptSort item
   Description: Call UpdateExt to delete BAQRptSort item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQRptSort
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param SortID Desc: SortID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BAQRptSorts_BAQRptID_SortID(BAQRptID:string, SortID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts(" + BAQRptID + "," + SortID + ")", {
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
   Description: Get BAQRptSortFlds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BAQRptSortFlds1
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param SortID Desc: SortID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptSortFldRow
   */  
export function get_BAQRptSorts_BAQRptID_SortID_BAQRptSortFlds(BAQRptID:string, SortID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortFldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts(" + BAQRptID + "," + SortID + ")/BAQRptSortFlds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortFldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BAQRptSortFld item
   Description: Calls GetByID to retrieve the BAQRptSortFld item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptSortFld1
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param SortID Desc: SortID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptSortFldRow
   */  
export function get_BAQRptSorts_BAQRptID_SortID_BAQRptSortFlds_BAQRptID_SortID_Seq(BAQRptID:string, SortID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQRptSortFldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSorts(" + BAQRptID + "," + SortID + ")/BAQRptSortFlds(" + BAQRptID + "," + SortID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQRptSortFldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get BAQRptSortFlds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BAQRptSortFlds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQRptSortFldRow
   */  
export function get_BAQRptSortFlds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortFldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSortFlds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortFldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BAQRptSortFlds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BAQRptSortFldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BAQRptSortFldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQRptSortFlds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSortFlds", {
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
   Summary: Calls GetByID to retrieve the BAQRptSortFld item
   Description: Calls GetByID to retrieve the BAQRptSortFld item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BAQRptSortFld
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param SortID Desc: SortID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BAQRptSortFldRow
   */  
export function get_BAQRptSortFlds_BAQRptID_SortID_Seq(BAQRptID:string, SortID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_BAQRptSortFldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSortFlds(" + BAQRptID + "," + SortID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_BAQRptSortFldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BAQRptSortFld for the service
   Description: Calls UpdateExt to update BAQRptSortFld. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BAQRptSortFld
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param SortID Desc: SortID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BAQRptSortFldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BAQRptSortFlds_BAQRptID_SortID_Seq(BAQRptID:string, SortID:string, Seq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSortFlds(" + BAQRptID + "," + SortID + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete BAQRptSortFld item
   Description: Call UpdateExt to delete BAQRptSortFld item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BAQRptSortFld
      @param BAQRptID Desc: BAQRptID   Required: True   Allow empty value : True
      @param SortID Desc: SortID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BAQRptSortFlds_BAQRptID_SortID_Seq(BAQRptID:string, SortID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/BAQRptSortFlds(" + BAQRptID + "," + SortID + "," + Seq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BAQReportListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQReportListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQReportListRow)
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
   Required: True   Allow empty value : True
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
export function get_GetRows(whereClauseBAQReport:string, whereClauseBAQRptOptionFld:string, whereClauseBAQRptFilter:string, whereClauseBAQRptSort:string, whereClauseBAQRptSortFld:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseBAQReport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBAQReport=" + whereClauseBAQReport
   }
   if(typeof whereClauseBAQRptOptionFld!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBAQRptOptionFld=" + whereClauseBAQRptOptionFld
   }
   if(typeof whereClauseBAQRptFilter!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBAQRptFilter=" + whereClauseBAQRptFilter
   }
   if(typeof whereClauseBAQRptSort!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBAQRptSort=" + whereClauseBAQRptSort
   }
   if(typeof whereClauseBAQRptSortFld!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBAQRptSortFld=" + whereClauseBAQRptSortFld
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetRows" + params, {
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
export function get_GetByID(baQRptID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof baQRptID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "baQRptID=" + baQRptID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetList" + params, {
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
   Summary: Invoke method CopyReport
   Description: This method makes a copy of an existing DynamicReport
   OperationID: CopyReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/CopyReport", {
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
   Summary: Invoke method GetListForBAQ
   Description: This method returns a list of reports that use a given BAQ
   OperationID: GetListForBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForBAQ(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetListForBAQ", {
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
   Summary: Invoke method ImportDynamicReport
   Description: This method imports a DynamicReport from the passed in dataset.
   OperationID: ImportDynamicReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportDynamicReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportDynamicReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportDynamicReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/ImportDynamicReport", {
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
   Summary: Invoke method GetAvailableFields
   Description: Gets the available query fields with the default report parameter columns.
Check01...10, Character01..05, Number01..05 and Date01..05.
   OperationID: GetAvailableFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetAvailableFields", {
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
   Summary: Invoke method ImportReportFile
   Description: Reads an imported BAQ report definition (as XML) from a shared folder.
   OperationID: ImportReportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportReportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportReportFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/ImportReportFile", {
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
   Summary: Invoke method ExportToFile
   Description: Exports the BAQ Report definition to an XML file.
   OperationID: ExportToFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportToFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportToFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportToFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/ExportToFile", {
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
   Summary: Invoke method GetSsrsConfigurationInformation
   Description: Gets the SSRS configuration information.
   OperationID: GetSsrsConfigurationInformation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSsrsConfigurationInformation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSsrsConfigurationInformation(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetSsrsConfigurationInformation", {
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
   Summary: Invoke method CreateReportFromTemplate
   Description: Creates the report based on the template.
   OperationID: CreateReportFromTemplate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateReportFromTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateReportFromTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateReportFromTemplate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/CreateReportFromTemplate", {
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
   Summary: Invoke method UpdateSsrsReport
   Description: Updates the report columns from the BAQ.
   OperationID: UpdateSsrsReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSsrsReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSsrsReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSsrsReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/UpdateSsrsReport", {
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
   Summary: Invoke method GetNewBAQReport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBAQReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetNewBAQReport", {
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
   Summary: Invoke method GetNewBAQRptOptionFld
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQRptOptionFld
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQRptOptionFld_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQRptOptionFld_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBAQRptOptionFld(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetNewBAQRptOptionFld", {
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
   Summary: Invoke method GetNewBAQRptFilter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQRptFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQRptFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQRptFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBAQRptFilter(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetNewBAQRptFilter", {
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
   Summary: Invoke method GetNewBAQRptSort
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQRptSort
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQRptSort_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQRptSort_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBAQRptSort(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetNewBAQRptSort", {
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
   Summary: Invoke method GetNewBAQRptSortFld
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBAQRptSortFld
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBAQRptSortFld_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBAQRptSortFld_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBAQRptSortFld(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetNewBAQRptSortFld", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicReportSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQReportListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQReportListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQReportRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQReportRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptFilterRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQRptFilterRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptOptionFldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQRptOptionFldRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortFldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQRptSortFldRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BAQRptSortRow{
   "odatametadata":string,
   "value":Ice_Tablesets_BAQRptSortRow[],
}

export interface Ice_Tablesets_BAQReportListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   "BAQRptID":string,
      /**  Description  */  
   "Description":string,
      /**  Title for this report  */  
   "ReportTitle":string,
      /**  The unique export identifier.  */  
   "ExportID":string,
      /**  Indicates the report is a system deliver report.  */  
   "SystemFlag":boolean,
      /**  true if this report is available to all companies  */  
   "GlobalReport":boolean,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BAQReportRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   "BAQRptID":string,
      /**  Description  */  
   "Description":string,
      /**  Title for this report  */  
   "ReportTitle":string,
      /**  Title for the report form  */  
   "FormTitle":string,
      /**  The unique export identifier.  */  
   "ExportID":string,
      /**  Indicates the report is a system deliver report.  */  
   "SystemFlag":boolean,
      /**  true if this report is completed, false if work in process  */  
   "Completed":boolean,
      /**  true if this report is available to all companies  */  
   "GlobalReport":boolean,
      /**  Indicates it is a crystal report.  */  
   "IsCrystalReport":boolean,
      /**  Report ID.  */  
   "ReportID":string,
      /**  Crystal Report Name  */  
   "CrystalReportName":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  SSRSReportName  */  
   "SSRSReportName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Temp Row ID  */  
   "TempRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BAQRptFilterRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   "BAQRptID":string,
      /**  BAQ Data Table  */  
   "DataTableID":string,
      /**  BAQ Field Name  */  
   "FieldName":string,
      /**  Adapter Name of the business object  */  
   "AdapterName":string,
      /**  Sequence of the Filter  */  
   "Seq":number,
      /**  The code field for a combobox.  */  
   "LookupField":string,
      /**  Label of the filter.  */  
   "FilterLabel":string,
      /**  Label that used on the filter panel.  */  
   "TabLabel":string,
      /**  Display name of the filter  */  
   "DisplayName":string,
      /**  GUID of the UI object  */  
   "EpiGuid":string,
      /**  Indicates if the filter is visible on the UI.  */  
   "IsVisible":boolean,
      /**  Field holding the filter value  */  
   "FilterField":string,
      /**  Indicates if the filter is a system delivered filter.  */  
   "SystemFlag":boolean,
      /**  Display order number  */  
   "DispOrder":number,
      /**  DataType  */  
   "DataType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Temp Row ID  */  
   "TempRowID":string,
   "FilterValue":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BAQRptOptionFldRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   "BAQRptID":string,
      /**  BAQ Data Table  */  
   "DataTableID":string,
      /**  BAQ Field Name  */  
   "FieldName":string,
      /**  Operator to use for relation between left value and right value.  */  
   "CompOp":string,
      /**  Sequence of the option  */  
   "Seq":number,
      /**  Default value for the option.  */  
   "DefaultValue":string,
      /**  Option field label.  */  
   "FieldLabel":string,
      /**  Display Name of the option  */  
   "DisplayName":string,
      /**  Field format  */  
   "FieldFormat":string,
      /**  GUID of the UI object  */  
   "EpiGuid":string,
      /**  Indicates if the option is visible on the UI.  */  
   "IsVisible":boolean,
      /**  Data type of the option field.  */  
   "DataType":string,
      /**  Indicates if the option is a system delivered option.  */  
   "SystemFlag":boolean,
      /**  Display order of the option.  */  
   "DispOrder":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "FieldValue":string,
      /**  Temp Row ID  */  
   "TempRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BAQRptSortFldRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   "BAQRptID":string,
      /**  The ID for this sort by  */  
   "SortID":string,
      /**  Indicates if the sort field is a system delivered sort field.  */  
   "SystemFlag":boolean,
      /**  BAQ Data Table  */  
   "DataTableID":string,
      /**  Sequence of the Sort Field  */  
   "Seq":number,
      /**  BAQ Field Name  */  
   "FieldName":string,
      /**  Indicates Ascending sort order when true  */  
   "IsAscending":boolean,
      /**  Display name  */  
   "DisplayName":string,
      /**  Display order of the sort field  */  
   "DispOrder":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Temp Row ID  */  
   "TempRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_BAQRptSortRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   "BAQRptID":string,
      /**  The ID for this sort by  */  
   "SortID":string,
      /**  Indicates if the sort is a system delivered sort.  */  
   "SystemFlag":boolean,
      /**  true if this sort by is the default  */  
   "IsDefault":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Temp Row ID  */  
   "TempRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param pcSourceRptID
      @param pcDestRptID
   */  
export interface CopyReport_input{
      /**  The source Report ID  */  
   pcSourceRptID:string,
      /**  The target Report ID  */  
   pcDestRptID:string,
}

export interface CopyReport_output{
parameters : {
      /**  output parameters  */  
   pbSucceed:boolean,
}
}

   /** Required : 
      @param baqRptID
   */  
export interface CreateReportFromTemplate_input{
      /**  The BAQRptID value.  */  
   baqRptID:string,
}

export interface CreateReportFromTemplate_output{
}

   /** Required : 
      @param baQRptID
   */  
export interface DeleteByID_input{
   baQRptID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param baqRptID
      @param newBaqRptID
      @param fileName
   */  
export interface ExportToFile_input{
      /**  The BAQ Report ID to export.  */  
   baqRptID:string,
      /**  The new BAQ Report ID (or empty if the existing ID is used).  */  
   newBaqRptID:string,
      /**  the fileName (relative path in UserData special folder)  */  
   fileName:string,
}

export interface ExportToFile_output{
}

   /** Required : 
      @param queryID
   */  
export interface GetAvailableFields_input{
      /**  the  */  
   queryID:string,
}

export interface GetAvailableFields_output{
   returnObj:Ice_Tablesets_DynamicQueryTableset[],
}

   /** Required : 
      @param baQRptID
   */  
export interface GetByID_input{
   baQRptID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_DynamicReportTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_DynamicReportTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_DynamicReportTableset[],
}

   /** Required : 
      @param pcBAQID
   */  
export interface GetListForBAQ_input{
      /**  The BAQ ID  */  
   pcBAQID:string,
}

export interface GetListForBAQ_output{
   returnObj:Ice_Tablesets_BAQReportListTableset[],
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
   returnObj:Ice_Tablesets_BAQReportListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewBAQReport_input{
   ds:Ice_Tablesets_DynamicReportTableset[],
}

export interface GetNewBAQReport_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DynamicReportTableset[],
}
}

   /** Required : 
      @param ds
      @param baQRptID
   */  
export interface GetNewBAQRptFilter_input{
   ds:Ice_Tablesets_DynamicReportTableset[],
   baQRptID:string,
}

export interface GetNewBAQRptFilter_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DynamicReportTableset[],
}
}

   /** Required : 
      @param ds
      @param baQRptID
   */  
export interface GetNewBAQRptOptionFld_input{
   ds:Ice_Tablesets_DynamicReportTableset[],
   baQRptID:string,
}

export interface GetNewBAQRptOptionFld_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DynamicReportTableset[],
}
}

   /** Required : 
      @param ds
      @param baQRptID
      @param sortID
   */  
export interface GetNewBAQRptSortFld_input{
   ds:Ice_Tablesets_DynamicReportTableset[],
   baQRptID:string,
   sortID:string,
}

export interface GetNewBAQRptSortFld_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DynamicReportTableset[],
}
}

   /** Required : 
      @param ds
      @param baQRptID
   */  
export interface GetNewBAQRptSort_input{
   ds:Ice_Tablesets_DynamicReportTableset[],
   baQRptID:string,
}

export interface GetNewBAQRptSort_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DynamicReportTableset[],
}
}

   /** Required : 
      @param whereClauseBAQReport
      @param whereClauseBAQRptOptionFld
      @param whereClauseBAQRptFilter
      @param whereClauseBAQRptSort
      @param whereClauseBAQRptSortFld
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseBAQReport:string,
   whereClauseBAQRptOptionFld:string,
   whereClauseBAQRptFilter:string,
   whereClauseBAQRptSort:string,
   whereClauseBAQRptSortFld:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_DynamicReportTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetSsrsConfigurationInformation_output{
parameters : {
      /**  output parameters  */  
   ssrsBaseUrl:string,
   rootFolder:string,
   webPortalUrl:string,
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

export interface Ice_Tablesets_BAQReportListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   BAQRptID:string,
      /**  Description  */  
   Description:string,
      /**  Title for this report  */  
   ReportTitle:string,
      /**  The unique export identifier.  */  
   ExportID:string,
      /**  Indicates the report is a system deliver report.  */  
   SystemFlag:boolean,
      /**  true if this report is available to all companies  */  
   GlobalReport:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQReportListTableset{
   BAQReportList:Ice_Tablesets_BAQReportListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BAQReportRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   BAQRptID:string,
      /**  Description  */  
   Description:string,
      /**  Title for this report  */  
   ReportTitle:string,
      /**  Title for the report form  */  
   FormTitle:string,
      /**  The unique export identifier.  */  
   ExportID:string,
      /**  Indicates the report is a system deliver report.  */  
   SystemFlag:boolean,
      /**  true if this report is completed, false if work in process  */  
   Completed:boolean,
      /**  true if this report is available to all companies  */  
   GlobalReport:boolean,
      /**  Indicates it is a crystal report.  */  
   IsCrystalReport:boolean,
      /**  Report ID.  */  
   ReportID:string,
      /**  Crystal Report Name  */  
   CrystalReportName:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  SSRSReportName  */  
   SSRSReportName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Temp Row ID  */  
   TempRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQRptFilterRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   BAQRptID:string,
      /**  BAQ Data Table  */  
   DataTableID:string,
      /**  BAQ Field Name  */  
   FieldName:string,
      /**  Adapter Name of the business object  */  
   AdapterName:string,
      /**  Sequence of the Filter  */  
   Seq:number,
      /**  The code field for a combobox.  */  
   LookupField:string,
      /**  Label of the filter.  */  
   FilterLabel:string,
      /**  Label that used on the filter panel.  */  
   TabLabel:string,
      /**  Display name of the filter  */  
   DisplayName:string,
      /**  GUID of the UI object  */  
   EpiGuid:string,
      /**  Indicates if the filter is visible on the UI.  */  
   IsVisible:boolean,
      /**  Field holding the filter value  */  
   FilterField:string,
      /**  Indicates if the filter is a system delivered filter.  */  
   SystemFlag:boolean,
      /**  Display order number  */  
   DispOrder:number,
      /**  DataType  */  
   DataType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Temp Row ID  */  
   TempRowID:string,
   FilterValue:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQRptOptionFldRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   BAQRptID:string,
      /**  BAQ Data Table  */  
   DataTableID:string,
      /**  BAQ Field Name  */  
   FieldName:string,
      /**  Operator to use for relation between left value and right value.  */  
   CompOp:string,
      /**  Sequence of the option  */  
   Seq:number,
      /**  Default value for the option.  */  
   DefaultValue:string,
      /**  Option field label.  */  
   FieldLabel:string,
      /**  Display Name of the option  */  
   DisplayName:string,
      /**  Field format  */  
   FieldFormat:string,
      /**  GUID of the UI object  */  
   EpiGuid:string,
      /**  Indicates if the option is visible on the UI.  */  
   IsVisible:boolean,
      /**  Data type of the option field.  */  
   DataType:string,
      /**  Indicates if the option is a system delivered option.  */  
   SystemFlag:boolean,
      /**  Display order of the option.  */  
   DispOrder:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   FieldValue:string,
      /**  Temp Row ID  */  
   TempRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQRptSortFldRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   BAQRptID:string,
      /**  The ID for this sort by  */  
   SortID:string,
      /**  Indicates if the sort field is a system delivered sort field.  */  
   SystemFlag:boolean,
      /**  BAQ Data Table  */  
   DataTableID:string,
      /**  Sequence of the Sort Field  */  
   Seq:number,
      /**  BAQ Field Name  */  
   FieldName:string,
      /**  Indicates Ascending sort order when true  */  
   IsAscending:boolean,
      /**  Display name  */  
   DisplayName:string,
      /**  Display order of the sort field  */  
   DispOrder:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Temp Row ID  */  
   TempRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_BAQRptSortRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  BAQ Report ID, the unique identifier for this report within the company  */  
   BAQRptID:string,
      /**  The ID for this sort by  */  
   SortID:string,
      /**  Indicates if the sort is a system delivered sort.  */  
   SystemFlag:boolean,
      /**  true if this sort by is the default  */  
   IsDefault:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Temp Row ID  */  
   TempRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DynamicQueryRow{
   Company:string,
   QueryID:string,
   AuthorID:string,
   Description:string,
   DisplayPhrase:string,
   IsShared:boolean,
   Version:string,
   CGCCode:string,
   XCompany:boolean,
   GlbCompany:string,
   Updatable:boolean,
   ExtQuery:boolean,
   ExtDatasourceName:string,
   SystemFlag:boolean,
   Extension:string,
   SysRevID:number,
   SysRowID:string,
   SecCode:string,
   AllCompanies:boolean,
   UseLiveDB:boolean,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_DynamicQueryTableset{
   DynamicQuery:Ice_Tablesets_DynamicQueryRow[],
   QueryCtrl:Ice_Tablesets_QueryCtrlRow[],
   QueryCtrlValues:Ice_Tablesets_QueryCtrlValuesRow[],
   QueryCustomAction:Ice_Tablesets_QueryCustomActionRow[],
   QueryExecuteSetting:Ice_Tablesets_QueryExecuteSettingRow[],
   QueryParameter:Ice_Tablesets_QueryParameterRow[],
   QueryReference:Ice_Tablesets_QueryReferenceRow[],
   QueryParameterBinding:Ice_Tablesets_QueryParameterBindingRow[],
   QuerySubQuery:Ice_Tablesets_QuerySubQueryRow[],
   QueryRelation:Ice_Tablesets_QueryRelationRow[],
   QueryRelationField:Ice_Tablesets_QueryRelationFieldRow[],
   QuerySortBy:Ice_Tablesets_QuerySortByRow[],
   QueryWhereItem:Ice_Tablesets_QueryWhereItemRow[],
   QueryGroupBy:Ice_Tablesets_QueryGroupByRow[],
   QueryTable:Ice_Tablesets_QueryTableRow[],
   QueryField:Ice_Tablesets_QueryFieldRow[],
   QueryFieldAttribute:Ice_Tablesets_QueryFieldAttributeRow[],
   QueryFunctionCall:Ice_Tablesets_QueryFunctionCallRow[],
   QueryUpdateField:Ice_Tablesets_QueryUpdateFieldRow[],
   QueryUpdateSettings:Ice_Tablesets_QueryUpdateSettingsRow[],
   QueryValueSetItems:Ice_Tablesets_QueryValueSetItemsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_DynamicReportTableset{
   BAQReport:Ice_Tablesets_BAQReportRow[],
   BAQRptOptionFld:Ice_Tablesets_BAQRptOptionFldRow[],
   BAQRptFilter:Ice_Tablesets_BAQRptFilterRow[],
   BAQRptSort:Ice_Tablesets_BAQRptSortRow[],
   BAQRptSortFld:Ice_Tablesets_BAQRptSortFldRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_QueryCtrlRow{
   Company:string,
   QueryID:string,
   ControlID:string,
   DataSource:string,
   DataType:string,
   FieldFormat:string,
   IsMandatory:boolean,
   DefaultValue:string,
   ControlType:string,
   SourceType:number,
   ListSource:string,
   DisplayColumn:string,
   ValueColumn:string,
   SysRevID:number,
   SysRowID:string,
   Seq:number,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryCtrlValuesRow{
   Company:string,
   QueryID:string,
   ControlID:string,
   ID:string,
   Val:string,
   Seq:number,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryCustomActionRow{
   Company:string,
   QueryID:string,
   ActionID:string,
   ActionLabel:string,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryExecuteSettingRow{
   Company:string,
   QueryID:string,
   SettingID:string,
   SettingValue:string,
   SystemFlag:boolean,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryFieldAttributeRow{
   Company:string,
   QueryID:string,
   SubQueryID:string,
   TableID:string,
   FieldName:string,
   AttributeName:string,
   Value:string,
   SystemFlag:boolean,
   SysRevID:number,
   SysRowID:string,
   IsOverriden:boolean,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryFieldRow{
   Company:string,
   QueryID:string,
   SubQueryID:string,
   TableID:string,
   FieldName:string,
   Seq:number,
   DBSchemaName:string,
   DBTableName:string,
   DBFieldName:string,
   DataType:string,
   Description:string,
   External:boolean,
   IsCalculated:boolean,
   Formula:string,
   FieldFormat:string,
   FieldLabel:string,
   LikeDataFieldTableID:string,
   LikeDataFieldSeq:number,
   Aggregation:string,
   IsGroupBy:boolean,
   UseLike:boolean,
   LikeDataFieldName:string,
   Updatable:boolean,
   RaiseEvent:boolean,
   QuickSearchID:string,
   DropDown:boolean,
   UpdInitExpression:string,
   Alias:string,
   SysRevID:number,
   SysRowID:string,
   DisplayName:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryFunctionCallRow{
   Company:string,
   QueryID:string,
   SubQueryID:string,
   FunctionID:string,
   ParameterName:string,
   Seq:number,
   Value:string,
   DataType:string,
   SystemFlag:boolean,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryGroupByRow{
   Company:string,
   QueryID:string,
   SubQueryID:string,
   GroupByID:string,
   Expression:string,
   Seq:number,
   SystemFlag:boolean,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryParameterBindingRow{
   Company:string,
   QueryID:string,
   ReferenceID:string,
   ParameterID:string,
   MappingType:string,
   MappingValue:string,
   SystemFlag:boolean,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryParameterRow{
   Company:string,
   QueryID:string,
   ParameterID:string,
   ParameterType:string,
   ParameterLabel:string,
   SkipIfEmpty:boolean,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryReferenceRow{
   Company:string,
   QueryID:string,
   ReferenceID:string,
   ReferenceName:string,
   RefQueryID:string,
   ExecType:string,
   SystemFlag:boolean,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryRelationFieldRow{
   Company:string,
   QueryID:string,
   SubQueryID:string,
   RelationID:string,
   Seq:number,
   ParentFieldName:string,
   ParentFieldDataType:string,
   ParentFieldIsExpr:boolean,
   ChildFieldName:string,
   ChildFieldDataType:string,
   ChildFieldIsExpr:boolean,
   AndOr:string,
   Neg:boolean,
   LeftP:string,
   RightP:string,
   CompOp:string,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryRelationRow{
   Company:string,
   QueryID:string,
   SubQueryID:string,
   RelationID:string,
   IsFK:boolean,
   ParentTableID:string,
   ChildTableID:string,
   JoinType:string,
   SysRevID:number,
   SysRowID:string,
   OuterJoin:boolean,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QuerySortByRow{
   Company:string,
   QueryID:string,
   SubQueryID:string,
   TableID:string,
   FieldName:string,
   Seq:number,
   IsAsc:boolean,
   SysRevID:number,
   SysRowID:string,
   DisplayName:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QuerySubQueryRow{
   Company:string,
   QueryID:string,
   SubQueryID:string,
   Name:string,
   Type:string,
   Seq:number,
   IsUnion:boolean,
   LeftP:string,
   RightP:string,
   SelectListClause:string,
   TopRowExpr:number,
   TopInPercent:boolean,
   TopWithTies:boolean,
   SysRevID:number,
   SysRowID:string,
   OrderByOffSet:string,
   OrderByFetch:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryTableRow{
   Company:string,
   QueryID:string,
   SubQueryID:string,
   TableID:string,
   Seq:number,
   DBSchemaName:string,
   DBTableName:string,
   TableType:string,
   IsSummaryTable:boolean,
   IsVisibleInDesigner:boolean,
   Modifiers:string,
   SystemFlag:boolean,
   SysRevID:number,
   SysRowID:string,
   PivotFunction:string,
   PivotDataType:string,
   PivotFieldFormat:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryUpdateFieldRow{
   Company:string,
   QueryID:string,
   MapTableName:string,
   MapFieldName:string,
   Direction:boolean,
   Expression:string,
   IsKeyField:boolean,
   SystemFlag:boolean,
   SysRevID:number,
   SysRowID:string,
   NetDataType:string,
   DataType:string,
   QualifiedName:string,
   Required:boolean,
   Description:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryUpdateSettingsRow{
   Company:string,
   QueryID:string,
   AllowAddNew:boolean,
   AddNewLabel:string,
   SupportMDR:boolean,
   UpdatableType:string,
   UpdatableBO:string,
   BOSystemCode:string,
   UpdateMethod:string,
   SCUrl:string,
   SCWorkflow:string,
   SCCtxUser:string,
   SCCtxPwd:string,
   SystemFlag:boolean,
   SysRevID:number,
   SysRowID:string,
   SCUserID:string,
   SCPassword:string,
   SCCtxUrl:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryValueSetItemsRow{
   Company:string,
   QueryID:string,
   ValueSetID:string,
   ItemValue:string,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_QueryWhereItemRow{
   Company:string,
   QueryID:string,
   SubQueryID:string,
   TableID:string,
   CriteriaID:string,
   Seq:number,
   FieldName:string,
   DataType:string,
   CompOp:string,
   AndOr:string,
   Neg:boolean,
   LeftP:string,
   RightP:string,
   IsConst:boolean,
   CriteriaType:number,
   ToTableID:string,
   ToFieldName:string,
   ToDataType:string,
   RValue:string,
   ExtSecurity:boolean,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Ice_Tablesets_UpdExtDynamicReportTableset{
   BAQReport:Ice_Tablesets_BAQReportRow[],
   BAQRptOptionFld:Ice_Tablesets_BAQRptOptionFldRow[],
   BAQRptFilter:Ice_Tablesets_BAQRptFilterRow[],
   BAQRptSort:Ice_Tablesets_BAQRptSortRow[],
   BAQRptSortFld:Ice_Tablesets_BAQRptSortFldRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface ImportDynamicReport_input{
   ds:Ice_Tablesets_DynamicReportTableset[],
}

export interface ImportDynamicReport_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DynamicReportTableset[],
   bOK:boolean,
}
}

   /** Required : 
      @param fileName
      @param baqRptID
   */  
export interface ImportReportFile_input{
      /**  the server filename (in UserData special folder).  */  
   fileName:string,
      /**  the BAQ Report ID (overrides the file).  */  
   baqRptID:string,
}

export interface ImportReportFile_output{
      /**  The BAQ Report ID.  */  
   returnObj:string,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtDynamicReportTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtDynamicReportTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param baqRptID
   */  
export interface UpdateSsrsReport_input{
      /**  The BAQRptID value.  */  
   baqRptID:string,
}

export interface UpdateSsrsReport_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_DynamicReportTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_DynamicReportTableset[],
}
}

