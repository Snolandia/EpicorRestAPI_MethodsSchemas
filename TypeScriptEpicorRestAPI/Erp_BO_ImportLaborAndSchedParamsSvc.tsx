import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ImportLaborAndSchedParamsSvc
// Description: Business Object for the Import of Labor and Scheduling Parameters
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/$metadata", {
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
   Description: Get ImportLaborAndSchedParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportLaborAndSchedParams
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImportGrpRow
   */  
export function get_ImportLaborAndSchedParams(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportLaborAndSchedParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportLaborAndSchedParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams", {
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
   Summary: Calls GetByID to retrieve the ImportLaborAndSchedParam item
   Description: Calls GetByID to retrieve the ImportLaborAndSchedParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportLaborAndSchedParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
   */  
export function get_ImportLaborAndSchedParams_Company_ImportID(Company:string, ImportID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ImportGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_ImportGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ImportLaborAndSchedParam for the service
   Description: Calls UpdateExt to update ImportLaborAndSchedParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportLaborAndSchedParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ImportLaborAndSchedParams_Company_ImportID(Company:string, ImportID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")", {
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
   Summary: Call UpdateExt to delete ImportLaborAndSchedParam item
   Description: Call UpdateExt to delete ImportLaborAndSchedParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportLaborAndSchedParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ImportLaborAndSchedParams_Company_ImportID(Company:string, ImportID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")", {
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
   Description: Get LaborHedImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborHedImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborHedImportRow
   */  
export function get_ImportLaborAndSchedParams_Company_ImportID_LaborHedImports(Company:string, ImportID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")/LaborHedImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborHedImport item
   Description: Calls GetByID to retrieve the LaborHedImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborHedImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborHedImportRow
   */  
export function get_ImportLaborAndSchedParams_Company_ImportID_LaborHedImports_Company_ImportID_LaborHedSeq(Company:string, ImportID:string, LaborHedSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborHedImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborHedImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get SchedParamImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SchedParamImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SchedParamImportRow
   */  
export function get_ImportLaborAndSchedParams_Company_ImportID_SchedParamImports(Company:string, ImportID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SchedParamImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")/SchedParamImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SchedParamImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SchedParamImport item
   Description: Calls GetByID to retrieve the SchedParamImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SchedParamImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param SchedParamSeq Desc: SchedParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SchedParamImportRow
   */  
export function get_ImportLaborAndSchedParams_Company_ImportID_SchedParamImports_Company_ImportID_SchedParamSeq(Company:string, ImportID:string, SchedParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SchedParamImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")/SchedParamImports(" + Company + "," + ImportID + "," + SchedParamSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SchedParamImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LaborHedImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborHedImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborHedImportRow
   */  
export function get_LaborHedImports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborHedImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborHedImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborHedImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborHedImports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports", {
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
   Summary: Calls GetByID to retrieve the LaborHedImport item
   Description: Calls GetByID to retrieve the LaborHedImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborHedImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborHedImportRow
   */  
export function get_LaborHedImports_Company_ImportID_LaborHedSeq(Company:string, ImportID:string, LaborHedSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborHedImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborHedImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborHedImport for the service
   Description: Calls UpdateExt to update LaborHedImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborHedImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborHedImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborHedImports_Company_ImportID_LaborHedSeq(Company:string, ImportID:string, LaborHedSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")", {
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
   Summary: Call UpdateExt to delete LaborHedImport item
   Description: Call UpdateExt to delete LaborHedImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborHedImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborHedImports_Company_ImportID_LaborHedSeq(Company:string, ImportID:string, LaborHedSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")", {
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
   Description: Get LaborDtlImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborDtlImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlImportRow
   */  
export function get_LaborHedImports_Company_ImportID_LaborHedSeq_LaborDtlImports(Company:string, ImportID:string, LaborHedSeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")/LaborDtlImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborDtlImport item
   Description: Calls GetByID to retrieve the LaborDtlImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlImportRow
   */  
export function get_LaborHedImports_Company_ImportID_LaborHedSeq_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LaborDtlImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtlImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlImportRow
   */  
export function get_LaborDtlImports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtlImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborDtlImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborDtlImports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports", {
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
   Summary: Calls GetByID to retrieve the LaborDtlImport item
   Description: Calls GetByID to retrieve the LaborDtlImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlImportRow
   */  
export function get_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborDtlImport for the service
   Description: Calls UpdateExt to update LaborDtlImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtlImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
   Summary: Call UpdateExt to delete LaborDtlImport item
   Description: Call UpdateExt to delete LaborDtlImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtlImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
   Description: Get LaborEquipImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborEquipImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborEquipImportRow
   */  
export function get_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_LaborEquipImports(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborEquipImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborEquipImport item
   Description: Calls GetByID to retrieve the LaborEquipImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborEquipImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborEquipImportRow
   */  
export function get_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_LaborEquipImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_EquipID(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, EquipID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborEquipImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborEquipImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborEquipImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LaborPartImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborPartImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborPartImportRow
   */  
export function get_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_LaborPartImports(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborPartImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborPartImport item
   Description: Calls GetByID to retrieve the LaborPartImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborPartImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborPartImportRow
   */  
export function get_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborPartImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborPartImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LaborEquipImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborEquipImports
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborEquipImportRow
   */  
export function get_LaborEquipImports(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborEquipImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborEquipImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborEquipImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborEquipImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborEquipImports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborEquipImports", {
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
   Summary: Calls GetByID to retrieve the LaborEquipImport item
   Description: Calls GetByID to retrieve the LaborEquipImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborEquipImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborEquipImportRow
   */  
export function get_LaborEquipImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_EquipID(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, EquipID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborEquipImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborEquipImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborEquipImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborEquipImport for the service
   Description: Calls UpdateExt to update LaborEquipImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborEquipImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborEquipImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborEquipImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_EquipID(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, EquipID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborEquipImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")", {
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
   Summary: Call UpdateExt to delete LaborEquipImport item
   Description: Call UpdateExt to delete LaborEquipImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborEquipImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborEquipImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_EquipID(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, EquipID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborEquipImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")", {
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
   Description: Get LaborPartImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborPartImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborPartImportRow
   */  
export function get_LaborPartImports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborPartImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborPartImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborPartImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborPartImports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports", {
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
   Summary: Calls GetByID to retrieve the LaborPartImport item
   Description: Calls GetByID to retrieve the LaborPartImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborPartImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborPartImportRow
   */  
export function get_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborPartImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborPartImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborPartImport for the service
   Description: Calls UpdateExt to update LaborPartImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborPartImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborPartImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")", {
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
   Summary: Call UpdateExt to delete LaborPartImport item
   Description: Call UpdateExt to delete LaborPartImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborPartImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")", {
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
   Description: Get LaborSerialNoImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborSerialNoImports1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborSerialNoImportRow
   */  
export function get_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_LaborSerialNoImports(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborSerialNoImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")/LaborSerialNoImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborSerialNoImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborSerialNoImport item
   Description: Calls GetByID to retrieve the LaborSerialNoImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborSerialNoImport1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborSerialNoImportRow
   */  
export function get_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_LaborSerialNoImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_SerialNumber(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborSerialNoImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")/LaborSerialNoImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborSerialNoImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LaborSerialNoImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborSerialNoImports
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborSerialNoImportRow
   */  
export function get_LaborSerialNoImports(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborSerialNoImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborSerialNoImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborSerialNoImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborSerialNoImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborSerialNoImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborSerialNoImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborSerialNoImports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborSerialNoImports", {
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
   Summary: Calls GetByID to retrieve the LaborSerialNoImport item
   Description: Calls GetByID to retrieve the LaborSerialNoImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborSerialNoImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborSerialNoImportRow
   */  
export function get_LaborSerialNoImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_SerialNumber(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, SerialNumber:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborSerialNoImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborSerialNoImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + "," + SerialNumber + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborSerialNoImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborSerialNoImport for the service
   Description: Calls UpdateExt to update LaborSerialNoImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborSerialNoImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborSerialNoImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborSerialNoImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_SerialNumber(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, SerialNumber:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborSerialNoImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + "," + SerialNumber + ")", {
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
   Summary: Call UpdateExt to delete LaborSerialNoImport item
   Description: Call UpdateExt to delete LaborSerialNoImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborSerialNoImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param SerialNumber Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborSerialNoImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_SerialNumber(Company:string, ImportID:string, LaborHedSeq:string, LaborDtlSeq:string, PartNum:string, SerialNumber:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborSerialNoImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + "," + SerialNumber + ")", {
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
   Description: Get SchedParamImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SchedParamImports
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SchedParamImportRow
   */  
export function get_SchedParamImports(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SchedParamImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/SchedParamImports", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SchedParamImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SchedParamImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SchedParamImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SchedParamImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SchedParamImports(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/SchedParamImports", {
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
   Summary: Calls GetByID to retrieve the SchedParamImport item
   Description: Calls GetByID to retrieve the SchedParamImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SchedParamImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param SchedParamSeq Desc: SchedParamSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SchedParamImportRow
   */  
export function get_SchedParamImports_Company_ImportID_SchedParamSeq(Company:string, ImportID:string, SchedParamSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SchedParamImportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/SchedParamImports(" + Company + "," + ImportID + "," + SchedParamSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_SchedParamImportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SchedParamImport for the service
   Description: Calls UpdateExt to update SchedParamImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SchedParamImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param SchedParamSeq Desc: SchedParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SchedParamImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SchedParamImports_Company_ImportID_SchedParamSeq(Company:string, ImportID:string, SchedParamSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/SchedParamImports(" + Company + "," + ImportID + "," + SchedParamSeq + ")", {
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
   Summary: Call UpdateExt to delete SchedParamImport item
   Description: Call UpdateExt to delete SchedParamImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SchedParamImport
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ImportID Desc: ImportID   Required: True   Allow empty value : True
      @param SchedParamSeq Desc: SchedParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SchedParamImports_Company_ImportID_SchedParamSeq(Company:string, ImportID:string, SchedParamSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/SchedParamImports(" + Company + "," + ImportID + "," + SchedParamSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImportGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpListRow)
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
export function get_GetRows(whereClauseImportGrp:string, whereClauseLaborHedImport:string, whereClauseLaborDtlImport:string, whereClauseLaborEquipImport:string, whereClauseLaborPartImport:string, whereClauseLaborSerialNoImport:string, whereClauseSchedParamImport:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseImportGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseImportGrp=" + whereClauseImportGrp
   }
   if(typeof whereClauseLaborHedImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborHedImport=" + whereClauseLaborHedImport
   }
   if(typeof whereClauseLaborDtlImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborDtlImport=" + whereClauseLaborDtlImport
   }
   if(typeof whereClauseLaborEquipImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborEquipImport=" + whereClauseLaborEquipImport
   }
   if(typeof whereClauseLaborPartImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborPartImport=" + whereClauseLaborPartImport
   }
   if(typeof whereClauseLaborSerialNoImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborSerialNoImport=" + whereClauseLaborSerialNoImport
   }
   if(typeof whereClauseSchedParamImport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSchedParamImport=" + whereClauseSchedParamImport
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(importID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof importID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "importID=" + importID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetList" + params, {
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
   Summary: Invoke method LaunchImport
   Description: Purpose: Launch the Import of Labor and Scheduling Parameters
   OperationID: LaunchImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LaunchImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LaunchImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaunchImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaunchImport", {
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
   Summary: Invoke method LaunchImportWithSummarizing
   Description: Purpose: Launch the Import of Labor and Scheduling Parameters.
Compared to the LaunchImport method, this version will implement logic to summarize the labor detail into one record until an employee sign-out signal is received.
The employee sign-out signal will close out the labor header and detail for that payroll date.
   OperationID: LaunchImportWithSummarizing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LaunchImportWithSummarizing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LaunchImportWithSummarizing_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaunchImportWithSummarizing(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaunchImportWithSummarizing", {
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
   Summary: Invoke method GetNewImportGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImportGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewImportGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetNewImportGrp", {
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
   Summary: Invoke method GetNewLaborHedImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborHedImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborHedImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborHedImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborHedImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetNewLaborHedImport", {
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
   Summary: Invoke method GetNewLaborDtlImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtlImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborDtlImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetNewLaborDtlImport", {
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
   Summary: Invoke method GetNewLaborEquipImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborEquipImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborEquipImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborEquipImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborEquipImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetNewLaborEquipImport", {
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
   Summary: Invoke method GetNewLaborPartImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborPartImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborPartImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborPartImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborPartImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetNewLaborPartImport", {
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
   Summary: Invoke method GetNewLaborSerialNoImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborSerialNoImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborSerialNoImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborSerialNoImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborSerialNoImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetNewLaborSerialNoImport", {
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
   Summary: Invoke method GetNewSchedParamImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSchedParamImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSchedParamImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSchedParamImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSchedParamImport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetNewSchedParamImport", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ImportGrpListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ImportGrpRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborDtlImportRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborEquipImportRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborHedImportRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborPartImportRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborSerialNoImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborSerialNoImportRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SchedParamImportRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SchedParamImportRow[],
}

export interface Erp_Tablesets_ImportGrpListRow{
      /**  Company  */  
   "Company":string,
      /**  ImportID  */  
   "ImportID":number,
      /**  ImportType  */  
   "ImportType":string,
      /**  ErrorFlag  */  
   "ErrorFlag":boolean,
      /**  Status  */  
   "Status":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "DisplayImportID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ImportGrpRow{
      /**  Company  */  
   "Company":string,
      /**  ImportID  */  
   "ImportID":number,
      /**  ImportType  */  
   "ImportType":string,
      /**  ErrorFlag  */  
   "ErrorFlag":boolean,
      /**  Status  */  
   "Status":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "IntError":boolean,
   "DisplayImportID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborDtlImportRow{
      /**  Company  */  
   "Company":string,
      /**  EmployeeNum  */  
   "EmployeeNum":string,
      /**  LaborHedSeq  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq  */  
   "LaborDtlSeq":number,
      /**  ImportID  */  
   "ImportID":number,
      /**  LaborType  */  
   "LaborType":string,
      /**  LaborTypePseudo  */  
   "LaborTypePseudo":string,
      /**  ReWork  */  
   "ReWork":boolean,
      /**  ReworkReasonCode  */  
   "ReworkReasonCode":string,
      /**  JobNum  */  
   "JobNum":string,
      /**  AssemblySeq  */  
   "AssemblySeq":number,
      /**  OprSeq  */  
   "OprSeq":number,
      /**  JCDept  */  
   "JCDept":string,
      /**  ResourceGrpID  */  
   "ResourceGrpID":string,
      /**  OpCode  */  
   "OpCode":string,
      /**  LaborHrs  */  
   "LaborHrs":number,
      /**  BurdenHrs  */  
   "BurdenHrs":number,
      /**  LaborQty  */  
   "LaborQty":number,
      /**  ScrapQty  */  
   "ScrapQty":number,
      /**  ScrapReasonCode  */  
   "ScrapReasonCode":string,
      /**  SetupPctComplete  */  
   "SetupPctComplete":number,
      /**  Complete  */  
   "Complete":boolean,
      /**  IndirectCode  */  
   "IndirectCode":string,
      /**  LaborNote  */  
   "LaborNote":string,
      /**  ExpenseCode  */  
   "ExpenseCode":string,
      /**  LaborCollection  */  
   "LaborCollection":boolean,
      /**  AppliedToSchedule  */  
   "AppliedToSchedule":boolean,
      /**  ClockInMInute  */  
   "ClockInMInute":number,
      /**  ClockOutMinute  */  
   "ClockOutMinute":number,
      /**  ClockInDate  */  
   "ClockInDate":string,
      /**  ClockinTime  */  
   "ClockinTime":number,
      /**  ClockOutTime  */  
   "ClockOutTime":number,
      /**  ActiveTrans  */  
   "ActiveTrans":boolean,
      /**  OverRidePayRate  */  
   "OverRidePayRate":number,
      /**  LaborRate  */  
   "LaborRate":number,
      /**  BurdenRate  */  
   "BurdenRate":number,
      /**  DspClockInTime  */  
   "DspClockInTime":string,
      /**  DspClockOutTime  */  
   "DspClockOutTime":string,
      /**  ResourceID  */  
   "ResourceID":string,
      /**  OpComplete  */  
   "OpComplete":boolean,
      /**  EarnedHrs  */  
   "EarnedHrs":number,
      /**  AddedOper  */  
   "AddedOper":boolean,
      /**  PayrollDate  */  
   "PayrollDate":string,
      /**  PostedToGL  */  
   "PostedToGL":boolean,
      /**  FiscalYear  */  
   "FiscalYear":number,
      /**  FiscalPeriod  */  
   "FiscalPeriod":number,
      /**  JournalNum  */  
   "JournalNum":number,
      /**  GLTrans  */  
   "GLTrans":boolean,
      /**  JournalCode  */  
   "JournalCode":string,
      /**  InspectionPending  */  
   "InspectionPending":boolean,
      /**  CallNum  */  
   "CallNum":number,
      /**  CallLine  */  
   "CallLine":number,
      /**  ServNum  */  
   "ServNum":number,
      /**  ServCode  */  
   "ServCode":string,
      /**  ResReasonCode  */  
   "ResReasonCode":string,
      /**  WipPosted  */  
   "WipPosted":boolean,
      /**  DiscrepQty  */  
   "DiscrepQty":number,
      /**  DiscrpRsnCode  */  
   "DiscrpRsnCode":string,
      /**  ParentLaborDtlSeq  */  
   "ParentLaborDtlSeq":number,
      /**  LaborEntryMethod  */  
   "LaborEntryMethod":string,
      /**  FiscalYearSuffix  */  
   "FiscalYearSuffix":string,
      /**  FiscalCalendarID  */  
   "FiscalCalendarID":string,
      /**  BFLaborReq  */  
   "BFLaborReq":boolean,
      /**  ABTUID  */  
   "ABTUID":string,
      /**  ProjectID  */  
   "ProjectID":string,
      /**  PhaseID  */  
   "PhaseID":string,
      /**  RoleCd  */  
   "RoleCd":string,
      /**  TimeTypCd  */  
   "TimeTypCd":string,
      /**  PBInvNum  */  
   "PBInvNum":number,
      /**  PMUID  */  
   "PMUID":number,
      /**  TaskSetID  */  
   "TaskSetID":string,
      /**  ApprovedDate  */  
   "ApprovedDate":string,
      /**  ClaimRef  */  
   "ClaimRef":string,
      /**  QuickEntryCode  */  
   "QuickEntryCode":string,
      /**  TimeStatus  */  
   "TimeStatus":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreateDate  */  
   "CreateDate":string,
      /**  CreateTime  */  
   "CreateTime":number,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
      /**  ChangeTime  */  
   "ChangeTime":number,
      /**  ActiveTaskID  */  
   "ActiveTaskID":string,
      /**  LastTaskID  */  
   "LastTaskID":string,
      /**  CreatedViaTEWeekView  */  
   "CreatedViaTEWeekView":boolean,
      /**  CurrentWFStageID  */  
   "CurrentWFStageID":string,
      /**  WFGroupID  */  
   "WFGroupID":string,
      /**  WFComplete  */  
   "WFComplete":boolean,
      /**  ApprovalRequired  */  
   "ApprovalRequired":boolean,
      /**  SubmittedBy  */  
   "SubmittedBy":string,
      /**  PBRateFrom  */  
   "PBRateFrom":string,
      /**  PBCurrencyCode  */  
   "PBCurrencyCode":string,
      /**  PBHours  */  
   "PBHours":number,
      /**  PBChargeRate  */  
   "PBChargeRate":number,
      /**  PBChargeAmt  */  
   "PBChargeAmt":number,
      /**  DocPBChargeRate  */  
   "DocPBChargeRate":number,
      /**  Rpt1PBChargeRate  */  
   "Rpt1PBChargeRate":number,
      /**  Rpt2PBChargeRate  */  
   "Rpt2PBChargeRate":number,
      /**  Rpt3PBChargeRate  */  
   "Rpt3PBChargeRate":number,
      /**  DocPBChargeAmt  */  
   "DocPBChargeAmt":number,
      /**  Rpt1PBChargeAmt  */  
   "Rpt1PBChargeAmt":number,
      /**  Rpt2PBChargeAmt  */  
   "Rpt2PBChargeAmt":number,
      /**  Rpt3PBChargeAmt  */  
   "Rpt3PBChargeAmt":number,
      /**  Shift  */  
   "Shift":number,
      /**  ActID  */  
   "ActID":number,
      /**  DtailID  */  
   "DtailID":number,
      /**  ProjProcessed  */  
   "ProjProcessed":boolean,
      /**  AsOfDate  */  
   "AsOfDate":string,
      /**  AsOfSeq  */  
   "AsOfSeq":number,
      /**  JDFInputFiles  */  
   "JDFInputFiles":string,
      /**  JDFNumberOfPages  */  
   "JDFNumberOfPages":string,
      /**  BatchWasSaved  */  
   "BatchWasSaved":string,
      /**  JDFCreatedByLink  */  
   "JDFCreatedByLink":boolean,
      /**  BatchComplete  */  
   "BatchComplete":boolean,
      /**  BatchRequestMove  */  
   "BatchRequestMove":boolean,
      /**  BatchPrint  */  
   "BatchPrint":boolean,
      /**  BatchLaborHrs  */  
   "BatchLaborHrs":number,
      /**  BatchPctOfTotHrs  */  
   "BatchPctOfTotHrs":number,
      /**  BatchQty  */  
   "BatchQty":number,
      /**  BatchTotalExpectedHrs  */  
   "BatchTotalExpectedHrs":number,
      /**  JDFOpCompleted  */  
   "JDFOpCompleted":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Downtime  */  
   "Downtime":boolean,
      /**  IntError  */  
   "IntError":boolean,
      /**  RefJobNum  */  
   "RefJobNum":string,
      /**  RefAssemblySeq  */  
   "RefAssemblySeq":number,
      /**  RefOprSeq  */  
   "RefOprSeq":number,
      /**  FSComplete  */  
   "FSComplete":boolean,
      /**  ErrorLog  */  
   "ErrorLog":string,
      /**  TimeAutoSubmit  */  
   "TimeAutoSubmit":boolean,
      /**  BatchMode  */  
   "BatchMode":boolean,
      /**  BillServiceRate  */  
   "BillServiceRate":number,
      /**  Used with the summarize labor detail function to signal employee sign-out.  When set to true will signal the labor import process to close out the current active labor header and detail for that payroll date.  */  
   "ExternalEmployeeSignedOut":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborEquipImportRow{
      /**  Company  */  
   "Company":string,
      /**  LaborHedSeq  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq  */  
   "LaborDtlSeq":number,
      /**  EquipID  */  
   "EquipID":string,
      /**  ImportID  */  
   "ImportID":number,
      /**  Hours  */  
   "Hours":number,
      /**  Qty  */  
   "Qty":number,
      /**  CurrentMeter  */  
   "CurrentMeter":number,
      /**  MeterUOM  */  
   "MeterUOM":string,
      /**  IntError  */  
   "IntError":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ErrorLog  */  
   "ErrorLog":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborHedImportRow{
      /**  Company  */  
   "Company":string,
      /**  EmployeeNum  */  
   "EmployeeNum":string,
      /**  LaborHedSeq  */  
   "LaborHedSeq":number,
      /**  ImportID  */  
   "ImportID":number,
      /**  PayrollDate  */  
   "PayrollDate":string,
      /**  Shift  */  
   "Shift":number,
      /**  ClockInDate  */  
   "ClockInDate":string,
      /**  ClockInTime  */  
   "ClockInTime":number,
      /**  DspClockInTime  */  
   "DspClockInTime":string,
      /**  ActualClockInTime  */  
   "ActualClockInTime":number,
      /**  ActualClockinDate  */  
   "ActualClockinDate":string,
      /**  LunchStatus  */  
   "LunchStatus":string,
      /**  ActLunchOutTime  */  
   "ActLunchOutTime":number,
      /**  LunchOutTime  */  
   "LunchOutTime":number,
      /**  ActLunchInTime  */  
   "ActLunchInTime":number,
      /**  LunchInTime  */  
   "LunchInTime":number,
      /**  ClockOutTime  */  
   "ClockOutTime":number,
      /**  DspClockOutTime  */  
   "DspClockOutTime":string,
      /**  ActualClockOutTime  */  
   "ActualClockOutTime":number,
      /**  PayHours  */  
   "PayHours":number,
      /**  FeedPayroll  */  
   "FeedPayroll":boolean,
      /**  TransferredToPayroll  */  
   "TransferredToPayroll":boolean,
      /**  LaborCollection  */  
   "LaborCollection":boolean,
      /**  TranSet  */  
   "TranSet":string,
      /**  ActiveTrans  */  
   "ActiveTrans":boolean,
      /**  ChkLink  */  
   "ChkLink":string,
      /**  BatchTotalHrsDisp  */  
   "BatchTotalHrsDisp":string,
      /**  BatchHrsRemainDisp  */  
   "BatchHrsRemainDisp":string,
      /**  BatchHrsRemainPctDisp  */  
   "BatchHrsRemainPctDisp":string,
      /**  BatchSplitHrsMethod  */  
   "BatchSplitHrsMethod":string,
      /**  BatchAssignTo  */  
   "BatchAssignTo":boolean,
      /**  BatchComplete  */  
   "BatchComplete":boolean,
      /**  BatchStartHrs  */  
   "BatchStartHrs":string,
      /**  BatchEndHrs  */  
   "BatchEndHrs":string,
      /**  BatchTotalHrs  */  
   "BatchTotalHrs":number,
      /**  BatchHrsRemain  */  
   "BatchHrsRemain":number,
      /**  BatchHrsRemainPct  */  
   "BatchHrsRemainPct":number,
      /**  IntError  */  
   "IntError":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ErrorLog  */  
   "ErrorLog":string,
      /**  BatchMode  */  
   "BatchMode":boolean,
      /**  HCMPayHoursCalcType  */  
   "HCMPayHoursCalcType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborPartImportRow{
      /**  Company  */  
   "Company":string,
      /**  LaborHedSeq  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq  */  
   "LaborDtlSeq":number,
      /**  PartNum  */  
   "PartNum":string,
      /**  ImportID  */  
   "ImportID":number,
      /**  PartQty  */  
   "PartQty":number,
      /**  IntError  */  
   "IntError":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ErrorLog  */  
   "ErrorLog":string,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   "DiscrepQty":number,
      /**  Discrepant Reason Code  */  
   "DiscrpRsnCode":string,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  */  
   "DiscrpAttributeSetID":number,
      /**  The reported scrap quantity.  */  
   "ScrapQty":number,
      /**  Scrap Reason Code  */  
   "ScrapReasonCode":string,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  */  
   "ScrapAttributeSetID":number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   "NonConfTranID":number,
      /**  The unique identifier of the related Dynamic Attribute Set for the PartQty  */  
   "LaborAttributeSetID":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborSerialNoImportRow{
      /**  Company  */  
   "Company":string,
      /**  LaborHedSeq  */  
   "LaborHedSeq":number,
      /**  LaborDtlSeq  */  
   "LaborDtlSeq":number,
      /**  PartNum  */  
   "PartNum":string,
      /**  SerialNumber  */  
   "SerialNumber":string,
      /**  ImportID  */  
   "ImportID":number,
      /**  JobNum  */  
   "JobNum":string,
      /**  AssemblySeq  */  
   "AssemblySeq":number,
      /**  OprSeq  */  
   "OprSeq":number,
      /**  SNStatus  */  
   "SNStatus":string,
      /**  IntError  */  
   "IntError":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ErrorLog  */  
   "ErrorLog":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SchedParamImportRow{
      /**  Company  */  
   "Company":string,
      /**  ImportID  */  
   "ImportID":number,
      /**  SchedParamSeq  */  
   "SchedParamSeq":number,
      /**  JobNum  */  
   "JobNum":string,
      /**  AssemblySeq  */  
   "AssemblySeq":number,
      /**  OprSeq  */  
   "OprSeq":number,
      /**  OpDtlSeq  */  
   "OpDtlSeq":number,
      /**  StartDate  */  
   "StartDate":string,
      /**  StartTime  */  
   "StartTime":number,
      /**  EndDate  */  
   "EndDate":string,
      /**  EndTime  */  
   "EndTime":number,
      /**  WhatIf  */  
   "WhatIf":boolean,
      /**  Finite  */  
   "Finite":boolean,
      /**  SchedTypeCode  */  
   "SchedTypeCode":string,
      /**  OverrideMtlCon  */  
   "OverrideMtlCon":boolean,
      /**  OverrideHistDateSetting  */  
   "OverrideHistDateSetting":number,
      /**  ScheduleDir  */  
   "ScheduleDir":boolean,
      /**  SuppressExceptions  */  
   "SuppressExceptions":boolean,
      /**  AllocNum  */  
   "AllocNum":number,
      /**  ResourceID  */  
   "ResourceID":string,
      /**  IntError  */  
   "IntError":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  ErrorLog  */  
   "ErrorLog":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param importID
   */  
export interface DeleteByID_input{
   importID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ImportGrpListRow{
      /**  Company  */  
   Company:string,
      /**  ImportID  */  
   ImportID:number,
      /**  ImportType  */  
   ImportType:string,
      /**  ErrorFlag  */  
   ErrorFlag:boolean,
      /**  Status  */  
   Status:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   DisplayImportID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ImportGrpRow{
      /**  Company  */  
   Company:string,
      /**  ImportID  */  
   ImportID:number,
      /**  ImportType  */  
   ImportType:string,
      /**  ErrorFlag  */  
   ErrorFlag:boolean,
      /**  Status  */  
   Status:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   IntError:boolean,
   DisplayImportID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ImportLaborAndSchedParamsErrorRow{
   Company:string,
   ImportID:number,
   ErrorLogLineText:string,
   ErrorLogLineNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ImportLaborAndSchedParamsErrorTableset{
   ImportLaborAndSchedParamsError:Erp_Tablesets_ImportLaborAndSchedParamsErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ImportLaborAndSchedParamsListTableset{
   ImportGrpList:Erp_Tablesets_ImportGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ImportLaborAndSchedParamsTableset{
   ImportGrp:Erp_Tablesets_ImportGrpRow[],
   LaborHedImport:Erp_Tablesets_LaborHedImportRow[],
   LaborDtlImport:Erp_Tablesets_LaborDtlImportRow[],
   LaborEquipImport:Erp_Tablesets_LaborEquipImportRow[],
   LaborPartImport:Erp_Tablesets_LaborPartImportRow[],
   LaborSerialNoImport:Erp_Tablesets_LaborSerialNoImportRow[],
   SchedParamImport:Erp_Tablesets_SchedParamImportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LaborDtlImportRow{
      /**  Company  */  
   Company:string,
      /**  EmployeeNum  */  
   EmployeeNum:string,
      /**  LaborHedSeq  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq  */  
   LaborDtlSeq:number,
      /**  ImportID  */  
   ImportID:number,
      /**  LaborType  */  
   LaborType:string,
      /**  LaborTypePseudo  */  
   LaborTypePseudo:string,
      /**  ReWork  */  
   ReWork:boolean,
      /**  ReworkReasonCode  */  
   ReworkReasonCode:string,
      /**  JobNum  */  
   JobNum:string,
      /**  AssemblySeq  */  
   AssemblySeq:number,
      /**  OprSeq  */  
   OprSeq:number,
      /**  JCDept  */  
   JCDept:string,
      /**  ResourceGrpID  */  
   ResourceGrpID:string,
      /**  OpCode  */  
   OpCode:string,
      /**  LaborHrs  */  
   LaborHrs:number,
      /**  BurdenHrs  */  
   BurdenHrs:number,
      /**  LaborQty  */  
   LaborQty:number,
      /**  ScrapQty  */  
   ScrapQty:number,
      /**  ScrapReasonCode  */  
   ScrapReasonCode:string,
      /**  SetupPctComplete  */  
   SetupPctComplete:number,
      /**  Complete  */  
   Complete:boolean,
      /**  IndirectCode  */  
   IndirectCode:string,
      /**  LaborNote  */  
   LaborNote:string,
      /**  ExpenseCode  */  
   ExpenseCode:string,
      /**  LaborCollection  */  
   LaborCollection:boolean,
      /**  AppliedToSchedule  */  
   AppliedToSchedule:boolean,
      /**  ClockInMInute  */  
   ClockInMInute:number,
      /**  ClockOutMinute  */  
   ClockOutMinute:number,
      /**  ClockInDate  */  
   ClockInDate:string,
      /**  ClockinTime  */  
   ClockinTime:number,
      /**  ClockOutTime  */  
   ClockOutTime:number,
      /**  ActiveTrans  */  
   ActiveTrans:boolean,
      /**  OverRidePayRate  */  
   OverRidePayRate:number,
      /**  LaborRate  */  
   LaborRate:number,
      /**  BurdenRate  */  
   BurdenRate:number,
      /**  DspClockInTime  */  
   DspClockInTime:string,
      /**  DspClockOutTime  */  
   DspClockOutTime:string,
      /**  ResourceID  */  
   ResourceID:string,
      /**  OpComplete  */  
   OpComplete:boolean,
      /**  EarnedHrs  */  
   EarnedHrs:number,
      /**  AddedOper  */  
   AddedOper:boolean,
      /**  PayrollDate  */  
   PayrollDate:string,
      /**  PostedToGL  */  
   PostedToGL:boolean,
      /**  FiscalYear  */  
   FiscalYear:number,
      /**  FiscalPeriod  */  
   FiscalPeriod:number,
      /**  JournalNum  */  
   JournalNum:number,
      /**  GLTrans  */  
   GLTrans:boolean,
      /**  JournalCode  */  
   JournalCode:string,
      /**  InspectionPending  */  
   InspectionPending:boolean,
      /**  CallNum  */  
   CallNum:number,
      /**  CallLine  */  
   CallLine:number,
      /**  ServNum  */  
   ServNum:number,
      /**  ServCode  */  
   ServCode:string,
      /**  ResReasonCode  */  
   ResReasonCode:string,
      /**  WipPosted  */  
   WipPosted:boolean,
      /**  DiscrepQty  */  
   DiscrepQty:number,
      /**  DiscrpRsnCode  */  
   DiscrpRsnCode:string,
      /**  ParentLaborDtlSeq  */  
   ParentLaborDtlSeq:number,
      /**  LaborEntryMethod  */  
   LaborEntryMethod:string,
      /**  FiscalYearSuffix  */  
   FiscalYearSuffix:string,
      /**  FiscalCalendarID  */  
   FiscalCalendarID:string,
      /**  BFLaborReq  */  
   BFLaborReq:boolean,
      /**  ABTUID  */  
   ABTUID:string,
      /**  ProjectID  */  
   ProjectID:string,
      /**  PhaseID  */  
   PhaseID:string,
      /**  RoleCd  */  
   RoleCd:string,
      /**  TimeTypCd  */  
   TimeTypCd:string,
      /**  PBInvNum  */  
   PBInvNum:number,
      /**  PMUID  */  
   PMUID:number,
      /**  TaskSetID  */  
   TaskSetID:string,
      /**  ApprovedDate  */  
   ApprovedDate:string,
      /**  ClaimRef  */  
   ClaimRef:string,
      /**  QuickEntryCode  */  
   QuickEntryCode:string,
      /**  TimeStatus  */  
   TimeStatus:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreateDate  */  
   CreateDate:string,
      /**  CreateTime  */  
   CreateTime:number,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  ChangeTime  */  
   ChangeTime:number,
      /**  ActiveTaskID  */  
   ActiveTaskID:string,
      /**  LastTaskID  */  
   LastTaskID:string,
      /**  CreatedViaTEWeekView  */  
   CreatedViaTEWeekView:boolean,
      /**  CurrentWFStageID  */  
   CurrentWFStageID:string,
      /**  WFGroupID  */  
   WFGroupID:string,
      /**  WFComplete  */  
   WFComplete:boolean,
      /**  ApprovalRequired  */  
   ApprovalRequired:boolean,
      /**  SubmittedBy  */  
   SubmittedBy:string,
      /**  PBRateFrom  */  
   PBRateFrom:string,
      /**  PBCurrencyCode  */  
   PBCurrencyCode:string,
      /**  PBHours  */  
   PBHours:number,
      /**  PBChargeRate  */  
   PBChargeRate:number,
      /**  PBChargeAmt  */  
   PBChargeAmt:number,
      /**  DocPBChargeRate  */  
   DocPBChargeRate:number,
      /**  Rpt1PBChargeRate  */  
   Rpt1PBChargeRate:number,
      /**  Rpt2PBChargeRate  */  
   Rpt2PBChargeRate:number,
      /**  Rpt3PBChargeRate  */  
   Rpt3PBChargeRate:number,
      /**  DocPBChargeAmt  */  
   DocPBChargeAmt:number,
      /**  Rpt1PBChargeAmt  */  
   Rpt1PBChargeAmt:number,
      /**  Rpt2PBChargeAmt  */  
   Rpt2PBChargeAmt:number,
      /**  Rpt3PBChargeAmt  */  
   Rpt3PBChargeAmt:number,
      /**  Shift  */  
   Shift:number,
      /**  ActID  */  
   ActID:number,
      /**  DtailID  */  
   DtailID:number,
      /**  ProjProcessed  */  
   ProjProcessed:boolean,
      /**  AsOfDate  */  
   AsOfDate:string,
      /**  AsOfSeq  */  
   AsOfSeq:number,
      /**  JDFInputFiles  */  
   JDFInputFiles:string,
      /**  JDFNumberOfPages  */  
   JDFNumberOfPages:string,
      /**  BatchWasSaved  */  
   BatchWasSaved:string,
      /**  JDFCreatedByLink  */  
   JDFCreatedByLink:boolean,
      /**  BatchComplete  */  
   BatchComplete:boolean,
      /**  BatchRequestMove  */  
   BatchRequestMove:boolean,
      /**  BatchPrint  */  
   BatchPrint:boolean,
      /**  BatchLaborHrs  */  
   BatchLaborHrs:number,
      /**  BatchPctOfTotHrs  */  
   BatchPctOfTotHrs:number,
      /**  BatchQty  */  
   BatchQty:number,
      /**  BatchTotalExpectedHrs  */  
   BatchTotalExpectedHrs:number,
      /**  JDFOpCompleted  */  
   JDFOpCompleted:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Downtime  */  
   Downtime:boolean,
      /**  IntError  */  
   IntError:boolean,
      /**  RefJobNum  */  
   RefJobNum:string,
      /**  RefAssemblySeq  */  
   RefAssemblySeq:number,
      /**  RefOprSeq  */  
   RefOprSeq:number,
      /**  FSComplete  */  
   FSComplete:boolean,
      /**  ErrorLog  */  
   ErrorLog:string,
      /**  TimeAutoSubmit  */  
   TimeAutoSubmit:boolean,
      /**  BatchMode  */  
   BatchMode:boolean,
      /**  BillServiceRate  */  
   BillServiceRate:number,
      /**  Used with the summarize labor detail function to signal employee sign-out.  When set to true will signal the labor import process to close out the current active labor header and detail for that payroll date.  */  
   ExternalEmployeeSignedOut:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborEquipImportRow{
      /**  Company  */  
   Company:string,
      /**  LaborHedSeq  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq  */  
   LaborDtlSeq:number,
      /**  EquipID  */  
   EquipID:string,
      /**  ImportID  */  
   ImportID:number,
      /**  Hours  */  
   Hours:number,
      /**  Qty  */  
   Qty:number,
      /**  CurrentMeter  */  
   CurrentMeter:number,
      /**  MeterUOM  */  
   MeterUOM:string,
      /**  IntError  */  
   IntError:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ErrorLog  */  
   ErrorLog:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborHedImportRow{
      /**  Company  */  
   Company:string,
      /**  EmployeeNum  */  
   EmployeeNum:string,
      /**  LaborHedSeq  */  
   LaborHedSeq:number,
      /**  ImportID  */  
   ImportID:number,
      /**  PayrollDate  */  
   PayrollDate:string,
      /**  Shift  */  
   Shift:number,
      /**  ClockInDate  */  
   ClockInDate:string,
      /**  ClockInTime  */  
   ClockInTime:number,
      /**  DspClockInTime  */  
   DspClockInTime:string,
      /**  ActualClockInTime  */  
   ActualClockInTime:number,
      /**  ActualClockinDate  */  
   ActualClockinDate:string,
      /**  LunchStatus  */  
   LunchStatus:string,
      /**  ActLunchOutTime  */  
   ActLunchOutTime:number,
      /**  LunchOutTime  */  
   LunchOutTime:number,
      /**  ActLunchInTime  */  
   ActLunchInTime:number,
      /**  LunchInTime  */  
   LunchInTime:number,
      /**  ClockOutTime  */  
   ClockOutTime:number,
      /**  DspClockOutTime  */  
   DspClockOutTime:string,
      /**  ActualClockOutTime  */  
   ActualClockOutTime:number,
      /**  PayHours  */  
   PayHours:number,
      /**  FeedPayroll  */  
   FeedPayroll:boolean,
      /**  TransferredToPayroll  */  
   TransferredToPayroll:boolean,
      /**  LaborCollection  */  
   LaborCollection:boolean,
      /**  TranSet  */  
   TranSet:string,
      /**  ActiveTrans  */  
   ActiveTrans:boolean,
      /**  ChkLink  */  
   ChkLink:string,
      /**  BatchTotalHrsDisp  */  
   BatchTotalHrsDisp:string,
      /**  BatchHrsRemainDisp  */  
   BatchHrsRemainDisp:string,
      /**  BatchHrsRemainPctDisp  */  
   BatchHrsRemainPctDisp:string,
      /**  BatchSplitHrsMethod  */  
   BatchSplitHrsMethod:string,
      /**  BatchAssignTo  */  
   BatchAssignTo:boolean,
      /**  BatchComplete  */  
   BatchComplete:boolean,
      /**  BatchStartHrs  */  
   BatchStartHrs:string,
      /**  BatchEndHrs  */  
   BatchEndHrs:string,
      /**  BatchTotalHrs  */  
   BatchTotalHrs:number,
      /**  BatchHrsRemain  */  
   BatchHrsRemain:number,
      /**  BatchHrsRemainPct  */  
   BatchHrsRemainPct:number,
      /**  IntError  */  
   IntError:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ErrorLog  */  
   ErrorLog:string,
      /**  BatchMode  */  
   BatchMode:boolean,
      /**  HCMPayHoursCalcType  */  
   HCMPayHoursCalcType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborPartImportRow{
      /**  Company  */  
   Company:string,
      /**  LaborHedSeq  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq  */  
   LaborDtlSeq:number,
      /**  PartNum  */  
   PartNum:string,
      /**  ImportID  */  
   ImportID:number,
      /**  PartQty  */  
   PartQty:number,
      /**  IntError  */  
   IntError:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ErrorLog  */  
   ErrorLog:string,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   DiscrepQty:number,
      /**  Discrepant Reason Code  */  
   DiscrpRsnCode:string,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  */  
   DiscrpAttributeSetID:number,
      /**  The reported scrap quantity.  */  
   ScrapQty:number,
      /**  Scrap Reason Code  */  
   ScrapReasonCode:string,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  */  
   ScrapAttributeSetID:number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfTranID:number,
      /**  The unique identifier of the related Dynamic Attribute Set for the PartQty  */  
   LaborAttributeSetID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborSerialNoImportRow{
      /**  Company  */  
   Company:string,
      /**  LaborHedSeq  */  
   LaborHedSeq:number,
      /**  LaborDtlSeq  */  
   LaborDtlSeq:number,
      /**  PartNum  */  
   PartNum:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  ImportID  */  
   ImportID:number,
      /**  JobNum  */  
   JobNum:string,
      /**  AssemblySeq  */  
   AssemblySeq:number,
      /**  OprSeq  */  
   OprSeq:number,
      /**  SNStatus  */  
   SNStatus:string,
      /**  IntError  */  
   IntError:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ErrorLog  */  
   ErrorLog:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SchedParamImportRow{
      /**  Company  */  
   Company:string,
      /**  ImportID  */  
   ImportID:number,
      /**  SchedParamSeq  */  
   SchedParamSeq:number,
      /**  JobNum  */  
   JobNum:string,
      /**  AssemblySeq  */  
   AssemblySeq:number,
      /**  OprSeq  */  
   OprSeq:number,
      /**  OpDtlSeq  */  
   OpDtlSeq:number,
      /**  StartDate  */  
   StartDate:string,
      /**  StartTime  */  
   StartTime:number,
      /**  EndDate  */  
   EndDate:string,
      /**  EndTime  */  
   EndTime:number,
      /**  WhatIf  */  
   WhatIf:boolean,
      /**  Finite  */  
   Finite:boolean,
      /**  SchedTypeCode  */  
   SchedTypeCode:string,
      /**  OverrideMtlCon  */  
   OverrideMtlCon:boolean,
      /**  OverrideHistDateSetting  */  
   OverrideHistDateSetting:number,
      /**  ScheduleDir  */  
   ScheduleDir:boolean,
      /**  SuppressExceptions  */  
   SuppressExceptions:boolean,
      /**  AllocNum  */  
   AllocNum:number,
      /**  ResourceID  */  
   ResourceID:string,
      /**  IntError  */  
   IntError:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  ErrorLog  */  
   ErrorLog:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtImportLaborAndSchedParamsTableset{
   ImportGrp:Erp_Tablesets_ImportGrpRow[],
   LaborHedImport:Erp_Tablesets_LaborHedImportRow[],
   LaborDtlImport:Erp_Tablesets_LaborDtlImportRow[],
   LaborEquipImport:Erp_Tablesets_LaborEquipImportRow[],
   LaborPartImport:Erp_Tablesets_LaborPartImportRow[],
   LaborSerialNoImport:Erp_Tablesets_LaborSerialNoImportRow[],
   SchedParamImport:Erp_Tablesets_SchedParamImportRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param importID
   */  
export interface GetByID_input{
   importID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
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
   returnObj:Erp_Tablesets_ImportLaborAndSchedParamsListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewImportGrp_input{
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}

export interface GetNewImportGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}
}

   /** Required : 
      @param ds
      @param importID
      @param laborHedSeq
   */  
export interface GetNewLaborDtlImport_input{
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
   importID:number,
   laborHedSeq:number,
}

export interface GetNewLaborDtlImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}
}

   /** Required : 
      @param ds
      @param importID
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetNewLaborEquipImport_input{
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
   importID:number,
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface GetNewLaborEquipImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}
}

   /** Required : 
      @param ds
      @param importID
   */  
export interface GetNewLaborHedImport_input{
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
   importID:number,
}

export interface GetNewLaborHedImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}
}

   /** Required : 
      @param ds
      @param importID
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetNewLaborPartImport_input{
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
   importID:number,
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface GetNewLaborPartImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}
}

   /** Required : 
      @param ds
      @param importID
      @param laborHedSeq
      @param laborDtlSeq
      @param partNum
   */  
export interface GetNewLaborSerialNoImport_input{
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
   importID:number,
   laborHedSeq:number,
   laborDtlSeq:number,
   partNum:string,
}

export interface GetNewLaborSerialNoImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}
}

   /** Required : 
      @param ds
      @param importID
   */  
export interface GetNewSchedParamImport_input{
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
   importID:number,
}

export interface GetNewSchedParamImport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}
}

   /** Required : 
      @param whereClauseImportGrp
      @param whereClauseLaborHedImport
      @param whereClauseLaborDtlImport
      @param whereClauseLaborEquipImport
      @param whereClauseLaborPartImport
      @param whereClauseLaborSerialNoImport
      @param whereClauseSchedParamImport
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseImportGrp:string,
   whereClauseLaborHedImport:string,
   whereClauseLaborDtlImport:string,
   whereClauseLaborEquipImport:string,
   whereClauseLaborPartImport:string,
   whereClauseLaborSerialNoImport:string,
   whereClauseSchedParamImport:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
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
      @param ipImportID
   */  
export interface LaunchImportWithSummarizing_input{
   ipImportID:number,
}

export interface LaunchImportWithSummarizing_output{
   returnObj:Erp_Tablesets_ImportLaborAndSchedParamsErrorTableset[],
}

   /** Required : 
      @param ipImportID
   */  
export interface LaunchImport_input{
   ipImportID:number,
}

export interface LaunchImport_output{
   returnObj:Erp_Tablesets_ImportLaborAndSchedParamsErrorTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtImportLaborAndSchedParamsTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtImportLaborAndSchedParamsTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportLaborAndSchedParamsTableset[],
}
}

