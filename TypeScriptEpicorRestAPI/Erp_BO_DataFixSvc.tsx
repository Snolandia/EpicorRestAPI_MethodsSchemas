import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.DataFixSvc
// Description: DataFix functionality
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/$metadata", {
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
   Description: Get DataFixes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataFixes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.datafixRow
   */  
export function get_DataFixes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_datafixRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_datafixRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataFixes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.datafixRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.datafixRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataFixes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes", {
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
   Summary: Calls GetByID to retrieve the DataFix item
   Description: Calls GetByID to retrieve the DataFix item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFix
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.datafixRow
   */  
export function get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_datafixRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_datafixRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataFix for the service
   Description: Calls UpdateExt to update DataFix. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataFix
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.datafixRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Summary: Call UpdateExt to delete DataFix item
   Description: Call UpdateExt to delete DataFix item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataFix
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Description: Get DataFixDDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataFixDDefs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixDDefRow
   */  
export function get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixDDefs(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixDDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixDDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixDDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataFixDDef item
   Description: Calls GetByID to retrieve the DataFixDDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixDDef1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tabseq Desc: tabseq   Required: True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqnum Desc: seqnum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixDDefRow
   */  
export function get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tabseq:string, tblname:string, seqnum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataFixDDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataFixDDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DataFixParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataFixParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixParamRow
   */  
export function get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixParams(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataFixParam item
   Description: Calls GetByID to retrieve the DataFixParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixParamRow
   */  
export function get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataFixParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataFixParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get DataFixRpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DataFixRpts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixRptRow
   */  
export function get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixRpts(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixRptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixRpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixRptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DataFixRpt item
   Description: Calls GetByID to retrieve the DataFixRpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixRpt1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqId Desc: seqId   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixRptRow
   */  
export function get_DataFixes_Company_LocalName_Key1_Key2_Key3_Key4_Key5_DataFixRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tblname:string, seqId:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataFixRptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixes(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/DataFixRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataFixRptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get DataFixDDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataFixDDefs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixDDefRow
   */  
export function get_DataFixDDefs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixDDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixDDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixDDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataFixDDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataFixDDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataFixDDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataFixDDefs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixDDefs", {
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
   Summary: Calls GetByID to retrieve the DataFixDDef item
   Description: Calls GetByID to retrieve the DataFixDDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixDDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tabseq Desc: tabseq   Required: True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqnum Desc: seqnum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixDDefRow
   */  
export function get_DataFixDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tabseq:string, tblname:string, seqnum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataFixDDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataFixDDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataFixDDef for the service
   Description: Calls UpdateExt to update DataFixDDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataFixDDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tabseq Desc: tabseq   Required: True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqnum Desc: seqnum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataFixDDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataFixDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tabseq:string, tblname:string, seqnum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")", {
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
   Summary: Call UpdateExt to delete DataFixDDef item
   Description: Call UpdateExt to delete DataFixDDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataFixDDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tabseq Desc: tabseq   Required: True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqnum Desc: seqnum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataFixDDefs_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tabseq_tblname_seqnum(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tabseq:string, tblname:string, seqnum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixDDefs(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tabseq + "," + tblname + "," + seqnum + ")", {
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
   Description: Get DataFixParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataFixParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixParamRow
   */  
export function get_DataFixParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataFixParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataFixParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataFixParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataFixParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixParams", {
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
   Summary: Calls GetByID to retrieve the DataFixParam item
   Description: Calls GetByID to retrieve the DataFixParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixParamRow
   */  
export function get_DataFixParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataFixParamRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataFixParamRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataFixParam for the service
   Description: Calls UpdateExt to update DataFixParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataFixParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataFixParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataFixParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Summary: Call UpdateExt to delete DataFixParam item
   Description: Call UpdateExt to delete DataFixParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataFixParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataFixParams_Company_LocalName_Key1_Key2_Key3_Key4_Key5(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixParams(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", {
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
   Description: Get DataFixRpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DataFixRpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DataFixRptRow
   */  
export function get_DataFixRpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixRptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixRpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixRptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DataFixRpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DataFixRptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DataFixRptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DataFixRpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixRpts", {
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
   Summary: Calls GetByID to retrieve the DataFixRpt item
   Description: Calls GetByID to retrieve the DataFixRpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DataFixRpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqId Desc: seqId   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DataFixRptRow
   */  
export function get_DataFixRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tblname:string, seqId:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_DataFixRptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_DataFixRptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update DataFixRpt for the service
   Description: Calls UpdateExt to update DataFixRpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DataFixRpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqId Desc: seqId   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DataFixRptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_DataFixRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tblname:string, seqId:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")", {
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
   Summary: Call UpdateExt to delete DataFixRpt item
   Description: Call UpdateExt to delete DataFixRpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DataFixRpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LocalName Desc: LocalName   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param tblname Desc: tblname   Required: True   Allow empty value : True
      @param seqId Desc: seqId   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_DataFixRpts_Company_LocalName_Key1_Key2_Key3_Key4_Key5_tblname_seqId(Company:string, LocalName:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, tblname:string, seqId:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DataFixRpts(" + Company + "," + LocalName + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + tblname + "," + seqId + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.datafixlistRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_datafixlistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_datafixlistRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausedatafix:string, whereClauseDataFixDDef:string, whereClauseDataFixParam:string, whereClauseDataFixRpt:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausedatafix!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausedatafix=" + whereClausedatafix
   }
   if(typeof whereClauseDataFixDDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataFixDDef=" + whereClauseDataFixDDef
   }
   if(typeof whereClauseDataFixParam!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataFixParam=" + whereClauseDataFixParam
   }
   if(typeof whereClauseDataFixRpt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDataFixRpt=" + whereClauseDataFixRpt
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(company:string, localName:string, key1:string, key2:string, key3:string, key4:string, key5:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof company!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "company=" + company
   }
   if(typeof localName!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "localName=" + localName
   }
   if(typeof key1!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key1=" + key1
   }
   if(typeof key2!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key2=" + key2
   }
   if(typeof key3!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key3=" + key3
   }
   if(typeof key4!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key4=" + key4
   }
   if(typeof key5!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "key5=" + key5
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetList" + params, {
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
   Summary: Invoke method GetByIDCustom
   Description: Get DataFix data for given DataFixId
   OperationID: GetByIDCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetByIDCustom", {
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
   Summary: Invoke method GetRowsCustom
   Description: Retrieve DataFix rows from Local001 table and populate temp tables
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCustom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetRowsCustom", {
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
   Summary: Invoke method StartReport
   Description: Start Report
   OperationID: StartReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StartReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StartReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StartReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/StartReport", {
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
   Summary: Invoke method UpdateReport
   Description: Update Report
   OperationID: UpdateReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/UpdateReport", {
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
   Summary: Invoke method CancelReport
   Description: Cancel Report
   OperationID: CancelReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/CancelReport", {
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
   Summary: Invoke method GetReport
   Description: Get Report
   OperationID: GetReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetReport", {
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
   Summary: Invoke method GetReportSysRowIDUpdate
   Description: Get Report
   OperationID: GetReportSysRowIDUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportSysRowIDUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportSysRowIDUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportSysRowIDUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetReportSysRowIDUpdate", {
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
   Summary: Invoke method ResetFix
   Description: Reset a Fix parameters and clear report
   OperationID: ResetFix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetFix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetFix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetFix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/ResetFix", {
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
   Summary: Invoke method SelectAll
   Description: Select all the current report records
   OperationID: SelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/SelectAll", {
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
   Summary: Invoke method UnSelectAll
   Description: UnSelect all the current report records
   OperationID: UnSelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnSelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnSelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnSelectAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/UnSelectAll", {
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
   Summary: Invoke method UnQuote
   Description: remove quotes from a string
   OperationID: UnQuote
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnQuote_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnQuote_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnQuote(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/UnQuote", {
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
   Summary: Invoke method RunUpdate
   Description: Run Data Fix Update
   OperationID: RunUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunUpdate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/RunUpdate", {
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
   Summary: Invoke method RunUpdateNoDisplay
   Description: Run Data Fix Update without displaying data first
   OperationID: RunUpdateNoDisplay
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunUpdateNoDisplay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunUpdateNoDisplay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunUpdateNoDisplay(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/RunUpdateNoDisplay", {
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
   Summary: Invoke method GetTenants
   Description: Get Tenants
   OperationID: GetTenants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTenants_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTenants_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTenants(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetTenants", {
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
   Summary: Invoke method GetCurrentTenantID
   Description: Get Current Tenant ID
   OperationID: GetCurrentTenantID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentTenantID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrentTenantID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetCurrentTenantID", {
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
   Summary: Invoke method GetInstallationID
   Description: Get Installation ID
   OperationID: GetInstallationID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstallationID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInstallationID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetInstallationID", {
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
   Summary: Invoke method GetCurrentInstallationID
   Description: Get Current Tenant ID
   OperationID: GetCurrentInstallationID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentInstallationID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrentInstallationID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetCurrentInstallationID", {
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
   Summary: Invoke method ImportDataFix
   Description: Import a new data fix
   OperationID: ImportDataFix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportDataFix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportDataFix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportDataFix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/ImportDataFix", {
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
   Summary: Invoke method PrereadDataFix
   OperationID: PrereadDataFix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrereadDataFix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrereadDataFix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrereadDataFix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/PrereadDataFix", {
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
   Summary: Invoke method GenerateParameterComponents
   Description: Generate the necessary components to fill parameters from ds.
   OperationID: GenerateParameterComponents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateParameterComponents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateParameterComponents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateParameterComponents(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GenerateParameterComponents", {
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
   Summary: Invoke method GetCompanies
   Description: Get the companies available.
   OperationID: GetCompanies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanies_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompanies(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetCompanies", {
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
   Summary: Invoke method UploadLocalImportFile
   OperationID: UploadLocalImportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadLocalImportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadLocalImportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadLocalImportFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/UploadLocalImportFile", {
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
   Summary: Invoke method GetRowsDataFix
   Description: Retrieve DataFix rows from Local001 table and populate temp tables
   OperationID: GetRowsDataFix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsDataFix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsDataFix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsDataFix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetRowsDataFix", {
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
   Summary: Invoke method GetNewdatafix
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewdatafix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewdatafix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewdatafix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewdatafix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetNewdatafix", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.DataFixSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixDDefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataFixDDefRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixParamRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataFixParamRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DataFixRptRow{
   "odatametadata":string,
   "value":Erp_Tablesets_DataFixRptRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_datafixRow{
   "odatametadata":string,
   "value":Erp_Tablesets_datafixRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_datafixlistRow{
   "odatametadata":string,
   "value":Erp_Tablesets_datafixlistRow[],
}

export interface Erp_Tablesets_DataFixDDefRow{
   "Company":string,
   "LocalName":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "seqnum":number,
   "datafixddefid":string,
   "tblname":string,
   "colname":string,
   "width":number,
   "datatype":string,
   "tabseq":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataFixParamRow{
   "Company":string,
   "LocalName":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "Label01":string,
   "Value01":string,
   "BlankOK01":boolean,
   "DataType01":string,
   "ViewType01":string,
   "Label02":string,
   "Value02":string,
   "BlankOK02":boolean,
   "DataType02":string,
   "ViewType02":string,
   "Label03":string,
   "Value03":string,
   "BlankOK03":boolean,
   "DataType03":string,
   "ViewType03":string,
   "Label04":string,
   "Value04":string,
   "BlankOK04":boolean,
   "DataType04":string,
   "ViewType04":string,
   "Label05":string,
   "Value05":string,
   "BlankOK05":boolean,
   "DataType05":string,
   "ViewType05":string,
   "Label06":string,
   "Value06":string,
   "BlankOK06":boolean,
   "DataType06":string,
   "ViewType06":string,
   "Label07":string,
   "Value07":string,
   "BlankOK07":boolean,
   "DataType07":string,
   "ViewType07":string,
   "Label08":string,
   "Value08":string,
   "BlankOK08":boolean,
   "DataType08":string,
   "ViewType08":string,
   "Label09":string,
   "Value09":string,
   "BlankOK09":boolean,
   "DataType09":string,
   "ViewType09":string,
   "Label10":string,
   "Value10":string,
   "BlankOK10":boolean,
   "DataType10":string,
   "ViewType10":string,
   "Label11":string,
   "Value11":string,
   "BlankOK11":boolean,
   "DataType11":string,
   "ViewType11":string,
   "Label12":string,
   "Value12":string,
   "BlankOK12":boolean,
   "DataType12":string,
   "ViewType12":string,
   "Label13":string,
   "Value13":string,
   "BlankOK13":boolean,
   "DataType13":string,
   "ViewType13":string,
   "Label14":string,
   "Value14":string,
   "BlankOK14":boolean,
   "DataType14":string,
   "ViewType14":string,
   "Label15":string,
   "Value15":string,
   "BlankOK15":boolean,
   "DataType15":string,
   "ViewType15":string,
   "Label16":string,
   "Value16":string,
   "BlankOK16":boolean,
   "DataType16":string,
   "ViewType16":string,
   "Label17":string,
   "Value17":string,
   "BlankOK17":boolean,
   "DataType17":string,
   "ViewType17":string,
   "Label18":string,
   "Value18":string,
   "BlankOK18":boolean,
   "DataType18":string,
   "ViewType18":string,
   "Label19":string,
   "Value19":string,
   "BlankOK19":boolean,
   "DataType19":string,
   "ViewType19":string,
   "Label20":string,
   "Value20":string,
   "BlankOK20":boolean,
   "DataType20":string,
   "ViewType20":string,
   "BlankCompOK":boolean,
   "LabelComp":string,
   "ViewTypeComp":string,
   "ValueComp":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_DataFixRptRow{
   "Company":string,
   "LocalName":string,
   "Key1":string,
   "Key2":string,
   "Key3":string,
   "Key4":string,
   "Key5":string,
   "UpdInd":boolean,
   "UpdTable":string,
   "value01":string,
   "value02":string,
   "value03":string,
   "value04":string,
   "value05":string,
   "value06":string,
   "value07":string,
   "value08":string,
   "value09":string,
   "value10":string,
   "value11":string,
   "value12":string,
   "value13":string,
   "value14":string,
   "value15":string,
   "value16":string,
   "value17":string,
   "value18":string,
   "value19":string,
   "value20":string,
   "value21":string,
   "value22":string,
   "value23":string,
   "value24":string,
   "value25":string,
   "value26":string,
   "value27":string,
   "value28":string,
   "value29":string,
   "value30":string,
   "value31":string,
   "value32":string,
   "value33":string,
   "value34":string,
   "value35":string,
   "value36":string,
   "value37":string,
   "value38":string,
   "value39":string,
   "value40":string,
   "value41":string,
   "value42":string,
   "value43":string,
   "value44":string,
   "value45":string,
   "value46":string,
   "value47":string,
   "value48":string,
   "value49":string,
   "value50":string,
   "value51":string,
   "value52":string,
   "value53":string,
   "value54":string,
   "value55":string,
   "value56":string,
   "value57":string,
   "value58":string,
   "value59":string,
   "value60":string,
   "value61":string,
   "value62":string,
   "value63":string,
   "value64":string,
   "value65":string,
   "value66":string,
   "value67":string,
   "value68":string,
   "value69":string,
   "value70":string,
   "value71":string,
   "value72":string,
   "value73":string,
   "value74":string,
   "value75":string,
   "value76":string,
   "value77":string,
   "value78":string,
   "value79":string,
   "value80":string,
   "value81":string,
   "value82":string,
   "value83":string,
   "value84":string,
   "value85":string,
   "value86":string,
   "value87":string,
   "value88":string,
   "value89":string,
   "value90":string,
   "value91":string,
   "value92":string,
   "value93":string,
   "value94":string,
   "value95":string,
   "value96":string,
   "value97":string,
   "value98":string,
   "value99":string,
   "seqId":number,
      /**  name of tab control record is displayed on  */  
   "tblname":string,
   "UpdXml":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_datafixRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Key field 5  */  
   "Key5":string,
      /**  Description  */  
   "Description":string,
      /**  Comments  */  
   "Comments":string,
      /**  Character01  */  
   "Character01":string,
   "Character02":string,
   "Character03":string,
   "Character04":string,
   "Character05":string,
   "Character06":string,
   "Character07":string,
   "Character08":string,
   "Character09":string,
   "Character10":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "Number06":number,
   "Number07":number,
   "Number08":number,
   "Number09":number,
   "Number10":number,
      /**  not used  */  
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "Number11":number,
   "Number12":number,
   "Number13":number,
   "Number14":number,
   "Number15":number,
   "Number16":number,
   "Number17":number,
   "Number18":number,
   "Number19":number,
   "Number20":number,
   "CheckBox06":boolean,
   "CheckBox07":boolean,
   "CheckBox08":boolean,
   "CheckBox09":boolean,
   "CheckBox10":boolean,
   "CheckBox11":boolean,
   "CheckBox12":boolean,
   "CheckBox13":boolean,
   "CheckBox14":boolean,
   "CheckBox15":boolean,
   "CheckBox16":boolean,
   "CheckBox17":boolean,
   "CheckBox18":boolean,
   "CheckBox19":boolean,
   "CheckBox20":boolean,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
   "ShortChar06":string,
   "ShortChar07":string,
   "ShortChar08":string,
   "ShortChar09":string,
   "ShortChar10":string,
   "ShortChar11":string,
   "ShortChar12":string,
   "ShortChar13":string,
   "ShortChar14":string,
   "ShortChar15":string,
   "ShortChar16":string,
   "ShortChar17":string,
   "ShortChar18":string,
   "ShortChar19":string,
   "ShortChar20":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "Available":boolean,
   "AvailDesc":string,
   "ExpiresInd":boolean,
   "Generic":boolean,
   "NotGeneric":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_datafixlistRow{
      /**  Company Code  */  
   "Company":string,
      /**  Localization Name  */  
   "LocalName":string,
      /**  Key field 1  */  
   "Key1":string,
      /**  Key field 2  */  
   "Key2":string,
      /**  Key field 3  */  
   "Key3":string,
      /**  Key field 4  */  
   "Key4":string,
      /**  Key field 5  */  
   "Key5":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "seqnum":number,
   "datafixddefid":string,
   "tblname":string,
   "colname":string,
   "width":number,
   "datatype":string,
   "tabseq":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param SysRowId
      @param DataFixId
      @param DataFixSPName
      @param PageSize
      @param ds
   */  
export interface CancelReport_input{
      /**  SysRowId of Data Fix record  */  
   SysRowId:string,
      /**  Data Fix ID  */  
   DataFixId:string,
      /**  Data Fix Stored Procedure  */  
   DataFixSPName:string,
      /**  Number of report records to return  */  
   PageSize:number,
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface CancelReport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param company
      @param localName
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
   */  
export interface DeleteByID_input{
   company:string,
   localName:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DataFixDDefRow{
   Company:string,
   LocalName:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   seqnum:number,
   datafixddefid:string,
   tblname:string,
   colname:string,
   width:number,
   datatype:string,
   tabseq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataFixListTableset{
   datafixlist:Erp_Tablesets_datafixlistRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_DataFixParamRow{
   Company:string,
   LocalName:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   Label01:string,
   Value01:string,
   BlankOK01:boolean,
   DataType01:string,
   ViewType01:string,
   Label02:string,
   Value02:string,
   BlankOK02:boolean,
   DataType02:string,
   ViewType02:string,
   Label03:string,
   Value03:string,
   BlankOK03:boolean,
   DataType03:string,
   ViewType03:string,
   Label04:string,
   Value04:string,
   BlankOK04:boolean,
   DataType04:string,
   ViewType04:string,
   Label05:string,
   Value05:string,
   BlankOK05:boolean,
   DataType05:string,
   ViewType05:string,
   Label06:string,
   Value06:string,
   BlankOK06:boolean,
   DataType06:string,
   ViewType06:string,
   Label07:string,
   Value07:string,
   BlankOK07:boolean,
   DataType07:string,
   ViewType07:string,
   Label08:string,
   Value08:string,
   BlankOK08:boolean,
   DataType08:string,
   ViewType08:string,
   Label09:string,
   Value09:string,
   BlankOK09:boolean,
   DataType09:string,
   ViewType09:string,
   Label10:string,
   Value10:string,
   BlankOK10:boolean,
   DataType10:string,
   ViewType10:string,
   Label11:string,
   Value11:string,
   BlankOK11:boolean,
   DataType11:string,
   ViewType11:string,
   Label12:string,
   Value12:string,
   BlankOK12:boolean,
   DataType12:string,
   ViewType12:string,
   Label13:string,
   Value13:string,
   BlankOK13:boolean,
   DataType13:string,
   ViewType13:string,
   Label14:string,
   Value14:string,
   BlankOK14:boolean,
   DataType14:string,
   ViewType14:string,
   Label15:string,
   Value15:string,
   BlankOK15:boolean,
   DataType15:string,
   ViewType15:string,
   Label16:string,
   Value16:string,
   BlankOK16:boolean,
   DataType16:string,
   ViewType16:string,
   Label17:string,
   Value17:string,
   BlankOK17:boolean,
   DataType17:string,
   ViewType17:string,
   Label18:string,
   Value18:string,
   BlankOK18:boolean,
   DataType18:string,
   ViewType18:string,
   Label19:string,
   Value19:string,
   BlankOK19:boolean,
   DataType19:string,
   ViewType19:string,
   Label20:string,
   Value20:string,
   BlankOK20:boolean,
   DataType20:string,
   ViewType20:string,
   BlankCompOK:boolean,
   LabelComp:string,
   ViewTypeComp:string,
   ValueComp:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataFixRptRow{
   Company:string,
   LocalName:string,
   Key1:string,
   Key2:string,
   Key3:string,
   Key4:string,
   Key5:string,
   UpdInd:boolean,
   UpdTable:string,
   value01:string,
   value02:string,
   value03:string,
   value04:string,
   value05:string,
   value06:string,
   value07:string,
   value08:string,
   value09:string,
   value10:string,
   value11:string,
   value12:string,
   value13:string,
   value14:string,
   value15:string,
   value16:string,
   value17:string,
   value18:string,
   value19:string,
   value20:string,
   value21:string,
   value22:string,
   value23:string,
   value24:string,
   value25:string,
   value26:string,
   value27:string,
   value28:string,
   value29:string,
   value30:string,
   value31:string,
   value32:string,
   value33:string,
   value34:string,
   value35:string,
   value36:string,
   value37:string,
   value38:string,
   value39:string,
   value40:string,
   value41:string,
   value42:string,
   value43:string,
   value44:string,
   value45:string,
   value46:string,
   value47:string,
   value48:string,
   value49:string,
   value50:string,
   value51:string,
   value52:string,
   value53:string,
   value54:string,
   value55:string,
   value56:string,
   value57:string,
   value58:string,
   value59:string,
   value60:string,
   value61:string,
   value62:string,
   value63:string,
   value64:string,
   value65:string,
   value66:string,
   value67:string,
   value68:string,
   value69:string,
   value70:string,
   value71:string,
   value72:string,
   value73:string,
   value74:string,
   value75:string,
   value76:string,
   value77:string,
   value78:string,
   value79:string,
   value80:string,
   value81:string,
   value82:string,
   value83:string,
   value84:string,
   value85:string,
   value86:string,
   value87:string,
   value88:string,
   value89:string,
   value90:string,
   value91:string,
   value92:string,
   value93:string,
   value94:string,
   value95:string,
   value96:string,
   value97:string,
   value98:string,
   value99:string,
   seqId:number,
      /**  name of tab control record is displayed on  */  
   tblname:string,
   UpdXml:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DataFixTableset{
   datafix:Erp_Tablesets_datafixRow[],
   DataFixDDef:Erp_Tablesets_DataFixDDefRow[],
   DataFixParam:Erp_Tablesets_DataFixParamRow[],
   DataFixRpt:Erp_Tablesets_DataFixRptRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ImportDataFixRow{
   DataFixId:string,
   FileName:string,
   FixDate:string,
   Imported:boolean,
   ImportMessage:string,
   RowNum:number,
   SysRowID:string,
   Title:string,
   UpdType:string,
   Version:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ImportDataFixTableset{
   ImportDataFix:Erp_Tablesets_ImportDataFixRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtDataFixTableset{
   datafix:Erp_Tablesets_datafixRow[],
   DataFixDDef:Erp_Tablesets_DataFixDDefRow[],
   DataFixParam:Erp_Tablesets_DataFixParamRow[],
   DataFixRpt:Erp_Tablesets_DataFixRptRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_datafixRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Key field 5  */  
   Key5:string,
      /**  Description  */  
   Description:string,
      /**  Comments  */  
   Comments:string,
      /**  Character01  */  
   Character01:string,
   Character02:string,
   Character03:string,
   Character04:string,
   Character05:string,
   Character06:string,
   Character07:string,
   Character08:string,
   Character09:string,
   Character10:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   Number06:number,
   Number07:number,
   Number08:number,
   Number09:number,
   Number10:number,
      /**  not used  */  
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   Number11:number,
   Number12:number,
   Number13:number,
   Number14:number,
   Number15:number,
   Number16:number,
   Number17:number,
   Number18:number,
   Number19:number,
   Number20:number,
   CheckBox06:boolean,
   CheckBox07:boolean,
   CheckBox08:boolean,
   CheckBox09:boolean,
   CheckBox10:boolean,
   CheckBox11:boolean,
   CheckBox12:boolean,
   CheckBox13:boolean,
   CheckBox14:boolean,
   CheckBox15:boolean,
   CheckBox16:boolean,
   CheckBox17:boolean,
   CheckBox18:boolean,
   CheckBox19:boolean,
   CheckBox20:boolean,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
   ShortChar06:string,
   ShortChar07:string,
   ShortChar08:string,
   ShortChar09:string,
   ShortChar10:string,
   ShortChar11:string,
   ShortChar12:string,
   ShortChar13:string,
   ShortChar14:string,
   ShortChar15:string,
   ShortChar16:string,
   ShortChar17:string,
   ShortChar18:string,
   ShortChar19:string,
   ShortChar20:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Available:boolean,
   AvailDesc:string,
   ExpiresInd:boolean,
   Generic:boolean,
   NotGeneric:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_datafixlistRow{
      /**  Company Code  */  
   Company:string,
      /**  Localization Name  */  
   LocalName:string,
      /**  Key field 1  */  
   Key1:string,
      /**  Key field 2  */  
   Key2:string,
      /**  Key field 3  */  
   Key3:string,
      /**  Key field 4  */  
   Key4:string,
      /**  Key field 5  */  
   Key5:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   seqnum:number,
   datafixddefid:string,
   tblname:string,
   colname:string,
   width:number,
   datatype:string,
   tabseq:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ds
   */  
export interface GenerateParameterComponents_input{
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface GenerateParameterComponents_output{
   returnObj:string,
}

   /** Required : 
      @param dataFixId
      @param PageSize
   */  
export interface GetByIDCustom_input{
      /**  The Data Fix Id  */  
   dataFixId:string,
      /**  number of report records to return  */  
   PageSize:number,
}

export interface GetByIDCustom_output{
   returnObj:Erp_Tablesets_DataFixTableset[],
}

   /** Required : 
      @param company
      @param localName
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
   */  
export interface GetByID_input{
   company:string,
   localName:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_DataFixTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_DataFixTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_DataFixTableset[],
}

export interface GetCompanies_output{
parameters : {
      /**  output parameters  */  
   companies:string,
}
}

export interface GetCurrentInstallationID_output{
   returnObj:string,
}

export interface GetCurrentTenantID_output{
   returnObj:string,
}

export interface GetInstallationID_output{
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
   returnObj:Erp_Tablesets_DataFixListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param company
      @param localName
      @param key1
      @param key2
      @param key3
      @param key4
   */  
export interface GetNewdatafix_input{
   ds:Erp_Tablesets_DataFixTableset[],
   company:string,
   localName:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
}

export interface GetNewdatafix_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param DataFixId
      @param DataFixSPName
      @param InstallationID
      @param PageSize
      @param ds
   */  
export interface GetReportSysRowIDUpdate_input{
      /**  Data Fix ID  */  
   DataFixId:string,
      /**  Data Fix Stored Procedure  */  
   DataFixSPName:string,
      /**  Install Id  */  
   InstallationID:string,
      /**  Number of Records to return  */  
   PageSize:number,
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface GetReportSysRowIDUpdate_output{
   returnObj:number,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param DataFixId
      @param DataFixSPName
      @param InstallationID
      @param PageSize
      @param ds
   */  
export interface GetReport_input{
      /**  Data Fix ID  */  
   DataFixId:string,
      /**  Data Fix Stored Procedure  */  
   DataFixSPName:string,
      /**  Install Id  */  
   InstallationID:string,
      /**  Number of Records to return  */  
   PageSize:number,
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface GetReport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param dataFixWhereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsCustom_input{
      /**  where clause for data fixes  */  
   dataFixWhereClause:string,
      /**  pagesize  */  
   pageSize:number,
      /**  Absolute page size  */  
   absolutePage:number,
}

export interface GetRowsCustom_output{
   returnObj:Erp_Tablesets_DataFixTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param dataFixWhereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsDataFix_input{
      /**  where clause for data fixes  */  
   dataFixWhereClause:string,
      /**  pagesize  */  
   pageSize:number,
      /**  Absolute page size  */  
   absolutePage:number,
}

export interface GetRowsDataFix_output{
   returnObj:Erp_Tablesets_DataFixTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausedatafix
      @param whereClauseDataFixDDef
      @param whereClauseDataFixParam
      @param whereClauseDataFixRpt
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausedatafix:string,
   whereClauseDataFixDDef:string,
   whereClauseDataFixParam:string,
   whereClauseDataFixRpt:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_DataFixTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param Tenants
      @param InstallIds
   */  
export interface GetTenants_input{
      /**  Tenant Ids  */  
   Tenants:string,
      /**  Install Ids  */  
   InstallIds:string,
}

export interface GetTenants_output{
parameters : {
      /**  output parameters  */  
   Tenants:string,
   InstallIds:string,
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
      @param DataFixId
      @param RetMessage
      @param DataFixData
   */  
export interface ImportDataFix_input{
      /**  Data Fix Id  */  
   DataFixId:string,
      /**  return message  */  
   RetMessage:string,
      /**  data fix data  */  
   DataFixData:string,
}

export interface ImportDataFix_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   RetMessage:string,
   DataFixData:any[],
}
}

   /** Required : 
      @param FileName
      @param FixData
      @param RetMessage
      @param ds
   */  
export interface PrereadDataFix_input{
   FileName:string,
   FixData:string,
   RetMessage:string,
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface PrereadDataFix_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   RetMessage:string,
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param DataFixId
      @param DataFixSPName
      @param SysRowId
      @param PageSize
      @param ds
   */  
export interface ResetFix_input{
      /**  Data Fix Id  */  
   DataFixId:string,
      /**  Data Fix Stored proc name  */  
   DataFixSPName:string,
      /**  SysRowId  */  
   SysRowId:string,
      /**  number of report records to return  */  
   PageSize:number,
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface ResetFix_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param DataFixId
      @param DataFixSPName
      @param ds
   */  
export interface RunUpdateNoDisplay_input{
      /**  Data Fix Id  */  
   DataFixId:string,
      /**  Data Fix Stored Proc Name  */  
   DataFixSPName:string,
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface RunUpdateNoDisplay_output{
parameters : {
      /**  output parameters  */  
   RptCnt:number,
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param DataFixId
      @param DataFixSPName
      @param ds
   */  
export interface RunUpdate_input{
      /**  Data Fix Id  */  
   DataFixId:string,
      /**  Data Fix Stored Proc Name  */  
   DataFixSPName:string,
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface RunUpdate_output{
parameters : {
      /**  output parameters  */  
   RptCnt:number,
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param DataFixId
      @param ds
   */  
export interface SelectAll_input{
      /**  Data Fix Id  */  
   DataFixId:string,
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface SelectAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param SysRowId
      @param DataFixId
      @param DataFixSPName
      @param InstallationID
      @param PageSize
      @param agentID
      @param ds
   */  
export interface StartReport_input{
      /**  SysRowId of Data Fix record  */  
   SysRowId:string,
      /**  Data Fix ID  */  
   DataFixId:string,
      /**  Data Fix Stored Procedure  */  
   DataFixSPName:string,
      /**  Install ID  */  
   InstallationID:string,
      /**  Number of Records to return  */  
   PageSize:number,
      /**  Task Agent  */  
   agentID:string,
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface StartReport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param avalue
   */  
export interface UnQuote_input{
      /**  string with quotes  */  
   avalue:string,
}

export interface UnQuote_output{
   returnObj:string,
}

   /** Required : 
      @param DataFixId
      @param ds
   */  
export interface UnSelectAll_input{
      /**  Data Fix Id  */  
   DataFixId:string,
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface UnSelectAll_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtDataFixTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtDataFixTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param SysRowId
      @param DataFixId
      @param DataFixSPName
      @param PageSize
      @param ds
   */  
export interface UpdateReport_input{
      /**  SysRowId of Data Fix record  */  
   SysRowId:string,
      /**  Data Fix ID  */  
   DataFixId:string,
      /**  Data Fix Stored Procedure  */  
   DataFixSPName:string,
      /**  Number of Records to return  */  
   PageSize:number,
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface UpdateReport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_DataFixTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DataFixTableset[],
}
}

   /** Required : 
      @param importFile
   */  
export interface UploadLocalImportFile_input{
   importFile:string,
}

export interface UploadLocalImportFile_output{
   returnObj:Erp_Tablesets_ImportDataFixTableset[],
}

