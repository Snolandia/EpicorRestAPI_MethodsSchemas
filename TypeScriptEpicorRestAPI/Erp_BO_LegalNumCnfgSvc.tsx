import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.LegalNumCnfgSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/$metadata", {
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
   Description: Get LegalNumCnfgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumCnfgs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumCnfgRow
   */  
export function get_LegalNumCnfgs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumCnfgRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumCnfgRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumCnfgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumCnfgRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumCnfgRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumCnfgs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs", {
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
   Summary: Calls GetByID to retrieve the LegalNumCnfg item
   Description: Calls GetByID to retrieve the LegalNumCnfg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumCnfg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumCnfgRow
   */  
export function get_LegalNumCnfgs_Company_LegalNumberID(Company:string, LegalNumberID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumCnfgRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumCnfgRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumCnfg for the service
   Description: Calls UpdateExt to update LegalNumCnfg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumCnfg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumCnfgRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumCnfgs_Company_LegalNumberID(Company:string, LegalNumberID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")", {
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
   Summary: Call UpdateExt to delete LegalNumCnfg item
   Description: Call UpdateExt to delete LegalNumCnfg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumCnfg
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumCnfgs_Company_LegalNumberID(Company:string, LegalNumberID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")", {
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
   Description: Get LegalNumDocTypes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LegalNumDocTypes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumDocTypeRow
   */  
export function get_LegalNumCnfgs_Company_LegalNumberID_LegalNumDocTypes(Company:string, LegalNumberID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumDocTypes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LegalNumDocType item
   Description: Calls GetByID to retrieve the LegalNumDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumDocType1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumDocTypeRow
   */  
export function get_LegalNumCnfgs_Company_LegalNumberID_LegalNumDocTypes_Company_LegalNumberID_TranDocTypeID(Company:string, LegalNumberID:string, TranDocTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumDocTypes(" + Company + "," + LegalNumberID + "," + TranDocTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LegalNumPrefixes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LegalNumPrefixes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumPrefixRow
   */  
export function get_LegalNumCnfgs_Company_LegalNumberID_LegalNumPrefixes(Company:string, LegalNumberID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumPrefixRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumPrefixes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumPrefixRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LegalNumPrefix item
   Description: Calls GetByID to retrieve the LegalNumPrefix item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumPrefix1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param Prefix Desc: Prefix   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumPrefixRow
   */  
export function get_LegalNumCnfgs_Company_LegalNumberID_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant(Company:string, LegalNumberID:string, Prefix:string, Plant:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumPrefixRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumPrefixRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get LegalNumSeqs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LegalNumSeqs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumSeqRow
   */  
export function get_LegalNumCnfgs_Company_LegalNumberID_LegalNumSeqs(Company:string, LegalNumberID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumSeqs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LegalNumSeq item
   Description: Calls GetByID to retrieve the LegalNumSeq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumSeq1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param DefaultPrefix Desc: DefaultPrefix   Required: True   Allow empty value : True
      @param TransYear Desc: TransYear   Required: True
      @param TransYearSuffix Desc: TransYearSuffix   Required: True   Allow empty value : True
      @param TransPeriod Desc: TransPeriod   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumSeqRow
   */  
export function get_LegalNumCnfgs_Company_LegalNumberID_LegalNumSeqs_Company_LegalNumberID_DefaultPrefix_TransYear_TransYearSuffix_TransPeriod_SysRowID(Company:string, LegalNumberID:string, DefaultPrefix:string, TransYear:string, TransYearSuffix:string, TransPeriod:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumSeqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumSeqs(" + Company + "," + LegalNumberID + "," + DefaultPrefix + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumSeqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LegalNumDocTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumDocTypes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumDocTypeRow
   */  
export function get_LegalNumDocTypes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumDocTypes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumDocTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumDocTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumDocTypes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumDocTypes", {
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
   Summary: Calls GetByID to retrieve the LegalNumDocType item
   Description: Calls GetByID to retrieve the LegalNumDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumDocTypeRow
   */  
export function get_LegalNumDocTypes_Company_LegalNumberID_TranDocTypeID(Company:string, LegalNumberID:string, TranDocTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumDocTypes(" + Company + "," + LegalNumberID + "," + TranDocTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumDocType for the service
   Description: Calls UpdateExt to update LegalNumDocType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumDocTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumDocTypes_Company_LegalNumberID_TranDocTypeID(Company:string, LegalNumberID:string, TranDocTypeID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumDocTypes(" + Company + "," + LegalNumberID + "," + TranDocTypeID + ")", {
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
   Summary: Call UpdateExt to delete LegalNumDocType item
   Description: Call UpdateExt to delete LegalNumDocType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumDocTypes_Company_LegalNumberID_TranDocTypeID(Company:string, LegalNumberID:string, TranDocTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumDocTypes(" + Company + "," + LegalNumberID + "," + TranDocTypeID + ")", {
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
   Description: Get LegalNumPrefixes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumPrefixes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumPrefixRow
   */  
export function get_LegalNumPrefixes(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumPrefixRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumPrefixRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumPrefixes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumPrefixRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumPrefixRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumPrefixes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes", {
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
   Summary: Calls GetByID to retrieve the LegalNumPrefix item
   Description: Calls GetByID to retrieve the LegalNumPrefix item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumPrefix
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param Prefix Desc: Prefix   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumPrefixRow
   */  
export function get_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant(Company:string, LegalNumberID:string, Prefix:string, Plant:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumPrefixRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumPrefixRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumPrefix for the service
   Description: Calls UpdateExt to update LegalNumPrefix. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumPrefix
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param Prefix Desc: Prefix   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumPrefixRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant(Company:string, LegalNumberID:string, Prefix:string, Plant:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete LegalNumPrefix item
   Description: Call UpdateExt to delete LegalNumPrefix item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumPrefix
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param Prefix Desc: Prefix   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant(Company:string, LegalNumberID:string, Prefix:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")", {
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
   Description: Get LegalNumSeqPrefixes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LegalNumSeqPrefixes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param Prefix Desc: Prefix   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumSeqPrefixRow
   */  
export function get_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant_LegalNumSeqPrefixes(Company:string, LegalNumberID:string, Prefix:string, Plant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqPrefixRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")/LegalNumSeqPrefixes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqPrefixRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LegalNumSeqPrefix item
   Description: Calls GetByID to retrieve the LegalNumSeqPrefix item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumSeqPrefix1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param Prefix Desc: Prefix   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param TransYear Desc: TransYear   Required: True
      @param TransYearSuffix Desc: TransYearSuffix   Required: True   Allow empty value : True
      @param TransPeriod Desc: TransPeriod   Required: True
      @param StartSequence Desc: StartSequence   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumSeqPrefixRow
   */  
export function get_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant_LegalNumSeqPrefixes_Company_LegalNumberID_Prefix_Plant_TransYear_TransYearSuffix_TransPeriod_StartSequence(Company:string, LegalNumberID:string, Prefix:string, Plant:string, TransYear:string, TransYearSuffix:string, TransPeriod:string, StartSequence:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumSeqPrefixRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")/LegalNumSeqPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + StartSequence + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumSeqPrefixRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LegalNumSeqPrefixes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumSeqPrefixes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumSeqPrefixRow
   */  
export function get_LegalNumSeqPrefixes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqPrefixRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqPrefixes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqPrefixRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumSeqPrefixes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqPrefixRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqPrefixRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumSeqPrefixes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqPrefixes", {
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
   Summary: Calls GetByID to retrieve the LegalNumSeqPrefix item
   Description: Calls GetByID to retrieve the LegalNumSeqPrefix item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumSeqPrefix
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param Prefix Desc: Prefix   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param TransYear Desc: TransYear   Required: True
      @param TransYearSuffix Desc: TransYearSuffix   Required: True   Allow empty value : True
      @param TransPeriod Desc: TransPeriod   Required: True
      @param StartSequence Desc: StartSequence   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumSeqPrefixRow
   */  
export function get_LegalNumSeqPrefixes_Company_LegalNumberID_Prefix_Plant_TransYear_TransYearSuffix_TransPeriod_StartSequence(Company:string, LegalNumberID:string, Prefix:string, Plant:string, TransYear:string, TransYearSuffix:string, TransPeriod:string, StartSequence:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumSeqPrefixRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + StartSequence + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumSeqPrefixRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumSeqPrefix for the service
   Description: Calls UpdateExt to update LegalNumSeqPrefix. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumSeqPrefix
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param Prefix Desc: Prefix   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param TransYear Desc: TransYear   Required: True
      @param TransYearSuffix Desc: TransYearSuffix   Required: True   Allow empty value : True
      @param TransPeriod Desc: TransPeriod   Required: True
      @param StartSequence Desc: StartSequence   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqPrefixRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumSeqPrefixes_Company_LegalNumberID_Prefix_Plant_TransYear_TransYearSuffix_TransPeriod_StartSequence(Company:string, LegalNumberID:string, Prefix:string, Plant:string, TransYear:string, TransYearSuffix:string, TransPeriod:string, StartSequence:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + StartSequence + ")", {
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
   Summary: Call UpdateExt to delete LegalNumSeqPrefix item
   Description: Call UpdateExt to delete LegalNumSeqPrefix item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumSeqPrefix
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param Prefix Desc: Prefix   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param TransYear Desc: TransYear   Required: True
      @param TransYearSuffix Desc: TransYearSuffix   Required: True   Allow empty value : True
      @param TransPeriod Desc: TransPeriod   Required: True
      @param StartSequence Desc: StartSequence   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumSeqPrefixes_Company_LegalNumberID_Prefix_Plant_TransYear_TransYearSuffix_TransPeriod_StartSequence(Company:string, LegalNumberID:string, Prefix:string, Plant:string, TransYear:string, TransYearSuffix:string, TransPeriod:string, StartSequence:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + StartSequence + ")", {
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
   Description: Get LegalNumSeqs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumSeqs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumSeqRow
   */  
export function get_LegalNumSeqs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumSeqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumSeqs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqs", {
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
   Summary: Calls GetByID to retrieve the LegalNumSeq item
   Description: Calls GetByID to retrieve the LegalNumSeq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumSeq
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param DefaultPrefix Desc: DefaultPrefix   Required: True   Allow empty value : True
      @param TransYear Desc: TransYear   Required: True
      @param TransYearSuffix Desc: TransYearSuffix   Required: True   Allow empty value : True
      @param TransPeriod Desc: TransPeriod   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumSeqRow
   */  
export function get_LegalNumSeqs_Company_LegalNumberID_DefaultPrefix_TransYear_TransYearSuffix_TransPeriod_SysRowID(Company:string, LegalNumberID:string, DefaultPrefix:string, TransYear:string, TransYearSuffix:string, TransPeriod:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumSeqRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqs(" + Company + "," + LegalNumberID + "," + DefaultPrefix + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumSeqRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumSeq for the service
   Description: Calls UpdateExt to update LegalNumSeq. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumSeq
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param DefaultPrefix Desc: DefaultPrefix   Required: True   Allow empty value : True
      @param TransYear Desc: TransYear   Required: True
      @param TransYearSuffix Desc: TransYearSuffix   Required: True   Allow empty value : True
      @param TransPeriod Desc: TransPeriod   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumSeqs_Company_LegalNumberID_DefaultPrefix_TransYear_TransYearSuffix_TransPeriod_SysRowID(Company:string, LegalNumberID:string, DefaultPrefix:string, TransYear:string, TransYearSuffix:string, TransPeriod:string, SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqs(" + Company + "," + LegalNumberID + "," + DefaultPrefix + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete LegalNumSeq item
   Description: Call UpdateExt to delete LegalNumSeq item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumSeq
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param DefaultPrefix Desc: DefaultPrefix   Required: True   Allow empty value : True
      @param TransYear Desc: TransYear   Required: True
      @param TransYearSuffix Desc: TransYearSuffix   Required: True   Allow empty value : True
      @param TransPeriod Desc: TransPeriod   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumSeqs_Company_LegalNumberID_DefaultPrefix_TransYear_TransYearSuffix_TransPeriod_SysRowID(Company:string, LegalNumberID:string, DefaultPrefix:string, TransYear:string, TransYearSuffix:string, TransPeriod:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqs(" + Company + "," + LegalNumberID + "," + DefaultPrefix + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + SysRowID + ")", {
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
   Description: Get AvailableDocTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AvailableDocTypes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AvailableDocTypeRow
   */  
export function get_AvailableDocTypes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AvailableDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableDocTypes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AvailableDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AvailableDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AvailableDocTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AvailableDocTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AvailableDocTypes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableDocTypes", {
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
   Summary: Calls GetByID to retrieve the AvailableDocType item
   Description: Calls GetByID to retrieve the AvailableDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AvailableDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AvailableDocTypeRow
   */  
export function get_AvailableDocTypes_Company_TranDocTypeID(Company:string, TranDocTypeID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AvailableDocTypeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableDocTypes(" + Company + "," + TranDocTypeID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AvailableDocTypeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AvailableDocType for the service
   Description: Calls UpdateExt to update AvailableDocType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AvailableDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AvailableDocTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AvailableDocTypes_Company_TranDocTypeID(Company:string, TranDocTypeID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableDocTypes(" + Company + "," + TranDocTypeID + ")", {
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
   Summary: Call UpdateExt to delete AvailableDocType item
   Description: Call UpdateExt to delete AvailableDocType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AvailableDocType
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param TranDocTypeID Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AvailableDocTypes_Company_TranDocTypeID(Company:string, TranDocTypeID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableDocTypes(" + Company + "," + TranDocTypeID + ")", {
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
   Description: Get AvailableLegalNumFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AvailableLegalNumFormats
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AvailableLegalNumFormatRow
   */  
export function get_AvailableLegalNumFormats(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AvailableLegalNumFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableLegalNumFormats", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AvailableLegalNumFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AvailableLegalNumFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AvailableLegalNumFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AvailableLegalNumFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AvailableLegalNumFormats(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableLegalNumFormats", {
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
   Summary: Calls GetByID to retrieve the AvailableLegalNumFormat item
   Description: Calls GetByID to retrieve the AvailableLegalNumFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AvailableLegalNumFormat
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AvailableLegalNumFormatRow
   */  
export function get_AvailableLegalNumFormats_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AvailableLegalNumFormatRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableLegalNumFormats(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_AvailableLegalNumFormatRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AvailableLegalNumFormat for the service
   Description: Calls UpdateExt to update AvailableLegalNumFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AvailableLegalNumFormat
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AvailableLegalNumFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AvailableLegalNumFormats_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableLegalNumFormats(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete AvailableLegalNumFormat item
   Description: Call UpdateExt to delete AvailableLegalNumFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AvailableLegalNumFormat
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AvailableLegalNumFormats_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableLegalNumFormats(" + SysRowID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumCnfgListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumCnfgListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumCnfgListRow)
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
export function get_GetRows(whereClauseLegalNumCnfg:string, whereClauseLegalNumDocType:string, whereClauseLegalNumPrefix:string, whereClauseLegalNumSeqPrefix:string, whereClauseLegalNumSeq:string, whereClauseAvailableDocType:string, whereClauseAvailableLegalNumFormat:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseLegalNumCnfg!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumCnfg=" + whereClauseLegalNumCnfg
   }
   if(typeof whereClauseLegalNumDocType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumDocType=" + whereClauseLegalNumDocType
   }
   if(typeof whereClauseLegalNumPrefix!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumPrefix=" + whereClauseLegalNumPrefix
   }
   if(typeof whereClauseLegalNumSeqPrefix!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumSeqPrefix=" + whereClauseLegalNumSeqPrefix
   }
   if(typeof whereClauseLegalNumSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumSeq=" + whereClauseLegalNumSeq
   }
   if(typeof whereClauseAvailableDocType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAvailableDocType=" + whereClauseAvailableDocType
   }
   if(typeof whereClauseAvailableLegalNumFormat!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAvailableLegalNumFormat=" + whereClauseAvailableLegalNumFormat
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetRows" + params, {
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
export function get_GetByID(legalNumberID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof legalNumberID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "legalNumberID=" + legalNumberID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetList" + params, {
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
   Description: CODE TO PROVIDE PUBLIC METHOD TO RETRIEVE THE CORRESPONDING LIST OF DESCRIPTIONS FOR A CODE FIELD
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetCodeDescList", {
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
   Summary: Invoke method GetTranDocType
   Description: This method return the TranDoctType that has not already assinged to legalNumber
   OperationID: GetTranDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTranDocType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetTranDocType", {
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
   Summary: Invoke method GetMXTaxRcptType
   Description: Getting Mexican Tax Receipt Type from Conpany configuration without parameters (by default)
   OperationID: GetMXTaxRcptType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMXTaxRcptType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMXTaxRcptType(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetMXTaxRcptType", {
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
   Summary: Invoke method OnChangeFormat
   Description: This method should be called if the Format changes.
   OperationID: OnChangeFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFormat(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeFormat", {
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
   Summary: Invoke method OnChangeGenSSCC
   Description: This method should be called if the Generate SSCC changes.
   OperationID: OnChangeGenSSCC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeGenSSCC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGenSSCC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeGenSSCC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeGenSSCC", {
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
   Summary: Invoke method OnChangeOfGenerationOption
   Description: This method is called when 'Generate On' (GenerationOption) is changed
   OperationID: OnChangeOfGenerationOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfGenerationOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfGenerationOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfGenerationOption(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeOfGenerationOption", {
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
   Summary: Invoke method OnChangeOfGenerationType
   Description: This method should be called if the Generation Type changes.
   OperationID: OnChangeOfGenerationType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfGenerationType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfGenerationType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfGenerationType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeOfGenerationType", {
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
   Summary: Invoke method OnChangeOfLegalNumberType
   Description: This method should be called after the LegalNumberType comboBox changes.
   OperationID: OnChangeOfLegalNumberType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumberType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumberType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfLegalNumberType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeOfLegalNumberType", {
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
   Summary: Invoke method OnChangeOfNumberOption
   Description: This method should be called after the NumberOption comboBox changes.
   OperationID: OnChangeOfNumberOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfNumberOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfNumberOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfNumberOption(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeOfNumberOption", {
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
   Summary: Invoke method OnChangeOfPrefixType
   Description: This method should be called if the Prefix Type changes.
   OperationID: OnChangeOfPrefixType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfPrefixType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfPrefixType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfPrefixType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeOfPrefixType", {
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
   Summary: Invoke method OnChangeOfLegalNumCnfgAutomaticVoiding
   Description: This method should be called after the Legal Number Configuration Automatic Voiding option changes.
   OperationID: OnChangeOfLegalNumCnfgAutomaticVoiding
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumCnfgAutomaticVoiding_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumCnfgAutomaticVoiding_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfLegalNumCnfgAutomaticVoiding(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeOfLegalNumCnfgAutomaticVoiding", {
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
   Summary: Invoke method OnChangeOfLegalNumPrefix
   Description: This method should be called if the LegalNumPrefix changes.
   OperationID: OnChangeOfLegalNumPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfLegalNumPrefix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeOfLegalNumPrefix", {
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
   Summary: Invoke method OnChangeOfLegalNumSeqEndSequence
   Description: This method should be called if the End Sequence changes.
   OperationID: OnChangeOfLegalNumSeqEndSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumSeqEndSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumSeqEndSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfLegalNumSeqEndSequence(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeOfLegalNumSeqEndSequence", {
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
   Summary: Invoke method OnChangeOfLegalNumSeqPrefixEndSequence
   Description: This method should be called if the End Sequence changes.
   OperationID: OnChangeOfLegalNumSeqPrefixEndSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumSeqPrefixEndSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumSeqPrefixEndSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfLegalNumSeqPrefixEndSequence(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeOfLegalNumSeqPrefixEndSequence", {
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
   Summary: Invoke method OnChangeOfLegalNumSeqStartSequence
   Description: This method should be called if the End Sequence changes.
   OperationID: OnChangeOfLegalNumSeqStartSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumSeqStartSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumSeqStartSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfLegalNumSeqStartSequence(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeOfLegalNumSeqStartSequence", {
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
   Summary: Invoke method OnChangeOfLegalNumSeqPrefixStartSequence
   Description: This method should be called if the End Sequence changes.
   OperationID: OnChangeOfLegalNumSeqPrefixStartSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumSeqPrefixStartSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumSeqPrefixStartSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfLegalNumSeqPrefixStartSequence(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/OnChangeOfLegalNumSeqPrefixStartSequence", {
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
   Summary: Invoke method ProcessPrefix
   Description: This method should be called after changing the default prefix.  This method
checks for a modified ttLegalNumCnfg record so an update shouldn't be done
before calling this method (it needs the modified record to see what the old
default prefix was).
It will check to see if sequences have been created using the old default
sequence.  If opMsgText is not returned as null, it should be displayed to the
user as a Yes/No question.  If the user answers "Yes" then the method RemoveSequences
should be called.
   OperationID: ProcessPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessPrefix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/ProcessPrefix", {
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
   Summary: Invoke method AltPrefixValidations
   Description: AltPrefixValidations
   OperationID: AltPrefixValidations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AltPrefixValidations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AltPrefixValidations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AltPrefixValidations(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AltPrefixValidations", {
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
   Summary: Invoke method RemoveAltPrefix
   Description: RemoveAltPrefix
   OperationID: RemoveAltPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveAltPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveAltPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveAltPrefix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/RemoveAltPrefix", {
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
   Summary: Invoke method RemoveSequences
   Description: This method should be called after calling the ProcessPrefix method and the user
answer "Yes" to the message returned from ProcessPrefix.  This method will remove
sequences that are using the old Default Prefix.
   OperationID: RemoveSequences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveSequences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveSequences_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveSequences(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/RemoveSequences", {
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
   Summary: Invoke method ResetTaxLegalNumber
   Description: This method will remove Legal Number and Tax Print Date from TaxTran and void Legal Number on LegalNumHistory Table.
   OperationID: ResetTaxLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetTaxLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetTaxLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResetTaxLegalNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/ResetTaxLegalNumber", {
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
   Summary: Invoke method RetrievePaymentInfo
   Description: This method will build the Payment information using the parameters
passed into the method.
   OperationID: RetrievePaymentInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrievePaymentInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrievePaymentInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetrievePaymentInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/RetrievePaymentInfo", {
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
   Summary: Invoke method VoidLegalNumCnfg
   Description: Purpose: Void Spoiled Legal Numbers.
Parameters:  dataset
Notes:
            
<param name="ds">legalNumCnfg is to used to set up the parameters used to generate legal numbers.</param>
   OperationID: VoidLegalNumCnfg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumCnfg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumCnfg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidLegalNumCnfg(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/VoidLegalNumCnfg", {
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
   Summary: Invoke method GetAvailableFormatElements
   Description: Load all Element available for the Legal Number format.
   OperationID: GetAvailableFormatElements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableFormatElements_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableFormatElements(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetAvailableFormatElements", {
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
   Summary: Invoke method GetAvailableFormatElementsExclExceedSeparators
   Description: Load all Element available for the Legal Number format.
   OperationID: GetAvailableFormatElementsExclExceedSeparators
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableFormatElementsExclExceedSeparators_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableFormatElementsExclExceedSeparators_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableFormatElementsExclExceedSeparators(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetAvailableFormatElementsExclExceedSeparators", {
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
   Summary: Invoke method GenerateLegalNumberSample
   Description: Generate Legal Number Sample
   OperationID: GenerateLegalNumberSample
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateLegalNumberSample_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateLegalNumberSample_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateLegalNumberSample(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GenerateLegalNumberSample", {
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
   Summary: Invoke method GetLegalNumberTypeList
   Description: Get list of Legal Number types
   OperationID: GetLegalNumberTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumberTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegalNumberTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetLegalNumberTypeList", {
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
   Summary: Invoke method GetChangeLogDetails
   Description: Get Change Log for specific Legal Number
   OperationID: GetChangeLogDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetChangeLogDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChangeLogDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetChangeLogDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetChangeLogDetails", {
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
   Summary: Invoke method GetNewLegalNumCnfg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumCnfg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumCnfg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumCnfg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLegalNumCnfg(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetNewLegalNumCnfg", {
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
   Summary: Invoke method GetNewLegalNumDocType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLegalNumDocType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetNewLegalNumDocType", {
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
   Summary: Invoke method GetNewLegalNumPrefix
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLegalNumPrefix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetNewLegalNumPrefix", {
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
   Summary: Invoke method GetNewLegalNumSeqPrefix
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumSeqPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumSeqPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumSeqPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLegalNumSeqPrefix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetNewLegalNumSeqPrefix", {
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
   Summary: Invoke method GetNewLegalNumSeq
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLegalNumSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetNewLegalNumSeq", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AvailableDocTypeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AvailableDocTypeRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AvailableLegalNumFormatRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AvailableLegalNumFormatRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumCnfgListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumCnfgListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumCnfgRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumCnfgRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumDocTypeRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumDocTypeRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumPrefixRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumPrefixRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqPrefixRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumSeqPrefixRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumSeqRow[],
}

export interface Erp_Tablesets_AvailableDocTypeRow{
   "Company":string,
   "Description":string,
   "SystemTranID":string,
   "TranDocTypeID":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_AvailableLegalNumFormatRow{
   "ElementCode":string,
   "ElementDesc":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumCnfgListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The legal number identifier.  */  
   "LegalNumberID":string,
      /**  Description  */  
   "Description":string,
      /**  The type of legal number.  */  
   "LegalNumberType":string,
      /**  The legal number prefix.  */  
   "DefaultPrefix":string,
      /**  Indicates how the number is generated.  Valid values are "system" and "manual".  */  
   "GenerationType":string,
      /**  For system generated numbers, indicates if the number should be displayed to the user immediately after generation.  */  
   "DispAfterGen":boolean,
      /**  Indicates if the prefix is user defined or a selected journal code.  Valid values are "user" or "jrnlcode".  */  
   "PrefixType":string,
      /**  For manual generation of legal numbers, indicates if the prefix can be overrided upon generation of the number.  */  
   "PrefixIsOverrideable":boolean,
      /**  Valid values are "Required" and "System".  */  
   "NumberOption":string,
      /**   The category of the legal number.  Valid options are:
DOC - Document legal number
TRAN - Transaction legal number  */  
   "LNCategory":string,
      /**  Allow prefixes to be defined at the Site level.  */  
   "AllowPrefixesByPlant":boolean,
      /**  Indicates if pre-printed documents are used for printing.  */  
   "UsePreNumberFmt":boolean,
      /**  Indicates if changes can be made to a document after it has been printed.  */  
   "AllowChangeAfterPrint":boolean,
      /**  Indicates the number of details lines that can be printed on a document per page.  */  
   "NumLineDetails":number,
      /**  Indicates if the year should be excluded when generating a legal number.  */  
   "ExcludeYrInNumber":boolean,
      /**  The separator symbol fof the pieces that make up a legal number.  */  
   "Separator":string,
      /**  Indicates if the legal number is active  */  
   "Inactive":boolean,
      /**  Reference to the fiscal calendar (Taiwan Localization field)  */  
   "FiscalCalendarID":string,
      /**  Exclude Period (Taiwan Localization field)  */  
   "ExcludePerInNumber":boolean,
      /**  The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  */  
   "ExtensionDigit":number,
      /**  Indicates if the Serial Shipment Container Code will be generated.  */  
   "GenSSCC":boolean,
      /**  The length that the sequence can be, user will be able to set it from 1 to 10. And it will be filled with leading zeros if the sequence doesnt fit the defined seq length.  */  
   "SeqLength":number,
      /**  Allow prefixes to be defined at Warehouse level.  */  
   "AllowPrefixesByWarehouse":boolean,
      /**  Allow prefixes to be defined at User level.  */  
   "AllowPrefixesByUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "JournalCode":string,
   "JrnlCodeJrnlDescription":string,
      /**  The type of legal number.  */  
   "LegalNumTypeDesc":string,
      /**  The old default Prefix  */  
   "OldDefaultPrefix":string,
      /**  The Reason of the void Legal Number Folios.  */  
   "VoidReason":string,
      /**  This field will be used to build Legal Number Folios.  */  
   "VoidYear":number,
      /**  Number of folios that start to be voided.  */  
   "FromFolio":string,
      /**  Last number of folios to be voided.  */  
   "ToFolio":string,
      /**  Inital sequence number from folio's number.  */  
   "FromSeq":number,
      /**  Last sequence number from folio's number.  */  
   "ToSeq":number,
   "FiscalCalDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumCnfgRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The legal number identifier.  */  
   "LegalNumberID":string,
      /**  Description  */  
   "Description":string,
      /**  The type of legal number.  */  
   "LegalNumberType":string,
      /**  The legal number prefix.  */  
   "DefaultPrefix":string,
      /**  Indicates how the number is generated.  Valid values are "system" and "manual".  */  
   "GenerationType":string,
      /**  For system generated numbers, indicates if the number should be displayed to the user immediately after generation.  */  
   "DispAfterGen":boolean,
      /**  Indicates if the prefix is user defined or a selected journal code.  Valid values are "user" or "jrnlcode".  */  
   "PrefixType":string,
      /**  For manual generation of legal numbers, indicates if the prefix can be overrided upon generation of the number.  */  
   "PrefixIsOverrideable":boolean,
      /**  Valid values are "Required" and "System".  */  
   "NumberOption":string,
      /**   The category of the legal number.  Valid options are:
DOC - Document legal number
TRAN - Transaction legal number  */  
   "LNCategory":string,
      /**  Allow prefixes to be defined at the Site level.  */  
   "AllowPrefixesByPlant":boolean,
      /**  Indicates if pre-printed documents are used for printing.  */  
   "UsePreNumberFmt":boolean,
      /**  Indicates if changes can be made to a document after it has been printed.  */  
   "AllowChangeAfterPrint":boolean,
      /**  Indicates the number of details lines that can be printed on a document per page.  */  
   "NumLineDetails":number,
      /**  Indicates if the year should be excluded when generating a legal number.  */  
   "ExcludeYrInNumber":boolean,
      /**  The separator symbol fof the pieces that make up a legal number.  */  
   "Separator":string,
      /**  Indicates if the legal number is active  */  
   "Inactive":boolean,
      /**  Reference to the fiscal calendar (Taiwan Localization field)  */  
   "FiscalCalendarID":string,
      /**  Exclude Period (Taiwan Localization field)  */  
   "ExcludePerInNumber":boolean,
      /**  The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  */  
   "ExtensionDigit":number,
      /**  Indicates if the Serial Shipment Container Code will be generated.  */  
   "GenSSCC":boolean,
      /**  The length that the sequence can be, user will be able to set it from 1 to 10. And it will be filled with leading zeros if the sequence doesnt fit the defined seq length.  */  
   "SeqLength":number,
      /**  Allow prefixes to be defined at Warehouse level.  */  
   "AllowPrefixesByWarehouse":boolean,
      /**  Allow prefixes to be defined at User level.  */  
   "AllowPrefixesByUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates when the legal number should be generated. Available options depend on the combination of Number Type and Generation Type selected for the Legal Number.  */  
   "GenerationOption":string,
      /**  Automatically void the legal number when the document is deleted  */  
   "AutomaticVoiding":boolean,
      /**  The automatic voiding text  */  
   "AutomaticVoidingText":string,
      /**  Use Change Log to track changes.  */  
   "ChangeLog":boolean,
      /**  Created By  */  
   "CreatedBy":string,
      /**  Created On  */  
   "CreatedOn":string,
      /**  Changed By  */  
   "ChangedBy":string,
      /**  Changed On  */  
   "ChangedOn":string,
      /**  Stores the format defined to generate the Legal Number.  */  
   "Format":string,
      /**  Separator is single character defined by user. It can be also used as Alternative Separator Character.  */  
   "ConditionalSeparator":string,
      /**  Free text defined by user to be used in Legal Numbers.  */  
   "FreeText":string,
      /**  Defines whether the Fiscal Year is displayed with 4  or 2 digits .  */  
   "FiscalYearFormat":string,
      /**  Defines whether the FiscalPeriod is displayed with 1, 2, o 3 digits.  */  
   "FiscalPeriodLength":number,
      /**  Defines if Day is displayed with leading zeros or not.  */  
   "AddLeadingZero":boolean,
      /**  Determines if Automatic Generate Option is enabled.  */  
   "EnableAutoGenerateOption":boolean,
      /**  Determines if Automatic Voiding Option is enabled.  */  
   "EnableAutoVoidOption":boolean,
   "FiscalCalDescription":string,
      /**  Number of folios that start to be voided.  */  
   "FromFolio":string,
      /**  Inital sequence number from folio's number.  */  
   "FromSeq":number,
   "JournalCode":string,
   "JrnlCodeJrnlDescription":string,
      /**  Foreign Key from LegalNumHistory Table used on Peru CSF as reference to run LegalNumberVoiding process  */  
   "LegalNumHistForeignKey":string,
      /**  Field for Peru CSF, Legal Number to be voided  */  
   "LegalNumHistLegalNumber":string,
   "LegalNumTypeDesc":string,
      /**  This field will specify the working mode of the digital tax receipt functionality. Will have three possible values: "CFD", "CFDI" and "Disabled".  */  
   "MXTaxRcptType":string,
      /**  The old default Prefix  */  
   "OldDefaultPrefix":string,
      /**  Check Number on payment, this field is used for Peru CSF  */  
   "PayCheckNum":number,
      /**  Document Check Amount on payment, this field is used for Peru CSF  */  
   "PayDocCheckAmt":number,
      /**  Tax Amount on payment, this field is used for Peru CSF  */  
   "PayDocTaxAmt":number,
      /**  Vendor ID on payment, this field is used for Peru CSF  */  
   "PayVendorID":string,
      /**  Vendor Name on payment, this field is used for Peru CSF  */  
   "PayVendorName":string,
      /**  Last number of folios to be voided.  */  
   "ToFolio":string,
      /**  Last sequence number from folio's number.  */  
   "ToSeq":number,
      /**  The Reason of the void Legal Number Folios.  */  
   "VoidReason":string,
      /**  This field will be used to build Legal Number Folios.  */  
   "VoidYear":number,
      /**  The list of automatic generation options  */  
   "AutomaticGenerationList":string,
   "LegalNumberSample":string,
      /**  Exclude Year in legal number format.  */  
   "ExcludeYear":boolean,
      /**  Exclude period in legal number format.  */  
   "ExcludePeriod":boolean,
   "INShippingPortCode":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumDocTypeRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The legal number identifier.  */  
   "LegalNumberID":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumPrefixRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The legal number identifier.  */  
   "LegalNumberID":string,
      /**  Prefix value for a legal number.  */  
   "Prefix":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Valid values are "Required" and "System".  */  
   "NumberOption":string,
      /**  Indicates if this is the default prefix for the legal number configuration.  */  
   "CnfgDefault":boolean,
      /**  User ID  */  
   "DcdUserID":string,
      /**  Warehouse used for the prefix  */  
   "WarehouseCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OldPrefix":string,
      /**  if Prefix is empty then [Blank Prefix] otherwise Prefix name.  */  
   "Description":string,
   "BitFlag":number,
   "plantName":string,
   "WarehseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumSeqPrefixRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The transaction year the sequence applies to.  Based on a calendar year.  */  
   "TransYear":number,
      /**  The transaction year suffix.  */  
   "TransYearSuffix":string,
      /**  The prefix used for this sequence when generating a legal number.  */  
   "Prefix":string,
      /**  The transaction period.  */  
   "TransPeriod":number,
      /**  The next available sequence number.  */  
   "NumberSeq":number,
      /**  The number of pre-printed forms available for the sequence.  */  
   "AvailFolios":number,
      /**  The number of folios used for this sequence.  */  
   "UsedFolios":number,
      /**  Start Sequence (Taiwan Localization field)  */  
   "StartSequence":number,
      /**  End Sequence (Taiwan Localization field)  */  
   "EndSequence":number,
      /**  Prefix used for the period. Available if TransPeriod > 0 (Taiwan Localization field)  */  
   "PeriodPrefix":string,
      /**  Inactive (Taiwan Localization field)  */  
   "Inactive":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGTableName  */  
   "AGTableName":string,
      /**  AGInvoiceNum  */  
   "AGInvoiceNum":number,
      /**  Approval Number (Mexico Localization field)  */  
   "MXApprovalNum":number,
      /**  Approval Year (Mexico Localization field)  */  
   "MXApprovalYear":number,
      /**  Expiration date for the sequence (Colombia Localization field)  */  
   "COExpirationDate":string,
   "CnfgDefault":boolean,
      /**  Used as reference to LegalNumPrefix, because the Prefix field has Period symbol in the end.  */  
   "DefaultPrefix":string,
   "LegalNumberID":string,
   "Plant":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumSeqRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The transaction year the sequence applies to.  Based on a calendar year.  */  
   "TransYear":number,
      /**  The transaction year suffix.  */  
   "TransYearSuffix":string,
      /**  The prefix used for this sequence when generating a legal number.  */  
   "Prefix":string,
      /**  The transaction period.  */  
   "TransPeriod":number,
      /**  The next available sequence number.  */  
   "NumberSeq":number,
      /**  The number of pre-printed forms available for the sequence.  */  
   "AvailFolios":number,
      /**  The number of folios used for this sequence.  */  
   "UsedFolios":number,
      /**  Start Sequence (Taiwan Localization field)  */  
   "StartSequence":number,
      /**  End Sequence (Taiwan Localization field)  */  
   "EndSequence":number,
      /**  Prefix used for the period. Available if TransPeriod > 0 (Taiwan Localization field)  */  
   "PeriodPrefix":string,
      /**  Inactive (Taiwan Localization field)  */  
   "Inactive":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGTableName  */  
   "AGTableName":string,
      /**  AGInvoiceNum  */  
   "AGInvoiceNum":number,
      /**  Approval Number (Mexico Localization field)  */  
   "MXApprovalNum":number,
      /**  Approval Year (Mexico Localization field)  */  
   "MXApprovalYear":number,
      /**  Expiration date for the sequence (Colombia Localization field)  */  
   "COExpirationDate":string,
   "DefaultPrefix":string,
   "LegalNumberID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipLegalNumberID
      @param ovPrefix
      @param plPrefix
      @param whPrefix
      @param usPrefix
      @param ds
   */  
export interface AltPrefixValidations_input{
   ipLegalNumberID:string,
   ovPrefix:boolean,
   plPrefix:boolean,
   whPrefix:boolean,
   usPrefix:boolean,
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface AltPrefixValidations_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
   altPrefixExists:boolean,
   opMsgText:string,
}
}

   /** Required : 
      @param legalNumberID
   */  
export interface DeleteByID_input{
   legalNumberID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AvailableDocTypeRow{
   Company:string,
   Description:string,
   SystemTranID:string,
   TranDocTypeID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AvailableLegalNumFormatRow{
   ElementCode:string,
   ElementDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ChangeLogRow{
   ChangeLogID:number,
   Company:string,
   SchemaName:string,
   TableName:string,
   CreatedBy:string,
   Action:string,
   Field:string,
   OldValue:string,
   NewValue:string,
   CreatedOn:string,
   FieldLabel:string,
   ForeignKey:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ChangeLogTableset{
   ChangeLog:Erp_Tablesets_ChangeLogRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LegalNumCnfgListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The legal number identifier.  */  
   LegalNumberID:string,
      /**  Description  */  
   Description:string,
      /**  The type of legal number.  */  
   LegalNumberType:string,
      /**  The legal number prefix.  */  
   DefaultPrefix:string,
      /**  Indicates how the number is generated.  Valid values are "system" and "manual".  */  
   GenerationType:string,
      /**  For system generated numbers, indicates if the number should be displayed to the user immediately after generation.  */  
   DispAfterGen:boolean,
      /**  Indicates if the prefix is user defined or a selected journal code.  Valid values are "user" or "jrnlcode".  */  
   PrefixType:string,
      /**  For manual generation of legal numbers, indicates if the prefix can be overrided upon generation of the number.  */  
   PrefixIsOverrideable:boolean,
      /**  Valid values are "Required" and "System".  */  
   NumberOption:string,
      /**   The category of the legal number.  Valid options are:
DOC - Document legal number
TRAN - Transaction legal number  */  
   LNCategory:string,
      /**  Allow prefixes to be defined at the Site level.  */  
   AllowPrefixesByPlant:boolean,
      /**  Indicates if pre-printed documents are used for printing.  */  
   UsePreNumberFmt:boolean,
      /**  Indicates if changes can be made to a document after it has been printed.  */  
   AllowChangeAfterPrint:boolean,
      /**  Indicates the number of details lines that can be printed on a document per page.  */  
   NumLineDetails:number,
      /**  Indicates if the year should be excluded when generating a legal number.  */  
   ExcludeYrInNumber:boolean,
      /**  The separator symbol fof the pieces that make up a legal number.  */  
   Separator:string,
      /**  Indicates if the legal number is active  */  
   Inactive:boolean,
      /**  Reference to the fiscal calendar (Taiwan Localization field)  */  
   FiscalCalendarID:string,
      /**  Exclude Period (Taiwan Localization field)  */  
   ExcludePerInNumber:boolean,
      /**  The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  */  
   ExtensionDigit:number,
      /**  Indicates if the Serial Shipment Container Code will be generated.  */  
   GenSSCC:boolean,
      /**  The length that the sequence can be, user will be able to set it from 1 to 10. And it will be filled with leading zeros if the sequence doesnt fit the defined seq length.  */  
   SeqLength:number,
      /**  Allow prefixes to be defined at Warehouse level.  */  
   AllowPrefixesByWarehouse:boolean,
      /**  Allow prefixes to be defined at User level.  */  
   AllowPrefixesByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   JournalCode:string,
   JrnlCodeJrnlDescription:string,
      /**  The type of legal number.  */  
   LegalNumTypeDesc:string,
      /**  The old default Prefix  */  
   OldDefaultPrefix:string,
      /**  The Reason of the void Legal Number Folios.  */  
   VoidReason:string,
      /**  This field will be used to build Legal Number Folios.  */  
   VoidYear:number,
      /**  Number of folios that start to be voided.  */  
   FromFolio:string,
      /**  Last number of folios to be voided.  */  
   ToFolio:string,
      /**  Inital sequence number from folio's number.  */  
   FromSeq:number,
      /**  Last sequence number from folio's number.  */  
   ToSeq:number,
   FiscalCalDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumCnfgListTableset{
   LegalNumCnfgList:Erp_Tablesets_LegalNumCnfgListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LegalNumCnfgRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The legal number identifier.  */  
   LegalNumberID:string,
      /**  Description  */  
   Description:string,
      /**  The type of legal number.  */  
   LegalNumberType:string,
      /**  The legal number prefix.  */  
   DefaultPrefix:string,
      /**  Indicates how the number is generated.  Valid values are "system" and "manual".  */  
   GenerationType:string,
      /**  For system generated numbers, indicates if the number should be displayed to the user immediately after generation.  */  
   DispAfterGen:boolean,
      /**  Indicates if the prefix is user defined or a selected journal code.  Valid values are "user" or "jrnlcode".  */  
   PrefixType:string,
      /**  For manual generation of legal numbers, indicates if the prefix can be overrided upon generation of the number.  */  
   PrefixIsOverrideable:boolean,
      /**  Valid values are "Required" and "System".  */  
   NumberOption:string,
      /**   The category of the legal number.  Valid options are:
DOC - Document legal number
TRAN - Transaction legal number  */  
   LNCategory:string,
      /**  Allow prefixes to be defined at the Site level.  */  
   AllowPrefixesByPlant:boolean,
      /**  Indicates if pre-printed documents are used for printing.  */  
   UsePreNumberFmt:boolean,
      /**  Indicates if changes can be made to a document after it has been printed.  */  
   AllowChangeAfterPrint:boolean,
      /**  Indicates the number of details lines that can be printed on a document per page.  */  
   NumLineDetails:number,
      /**  Indicates if the year should be excluded when generating a legal number.  */  
   ExcludeYrInNumber:boolean,
      /**  The separator symbol fof the pieces that make up a legal number.  */  
   Separator:string,
      /**  Indicates if the legal number is active  */  
   Inactive:boolean,
      /**  Reference to the fiscal calendar (Taiwan Localization field)  */  
   FiscalCalendarID:string,
      /**  Exclude Period (Taiwan Localization field)  */  
   ExcludePerInNumber:boolean,
      /**  The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  */  
   ExtensionDigit:number,
      /**  Indicates if the Serial Shipment Container Code will be generated.  */  
   GenSSCC:boolean,
      /**  The length that the sequence can be, user will be able to set it from 1 to 10. And it will be filled with leading zeros if the sequence doesnt fit the defined seq length.  */  
   SeqLength:number,
      /**  Allow prefixes to be defined at Warehouse level.  */  
   AllowPrefixesByWarehouse:boolean,
      /**  Allow prefixes to be defined at User level.  */  
   AllowPrefixesByUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates when the legal number should be generated. Available options depend on the combination of Number Type and Generation Type selected for the Legal Number.  */  
   GenerationOption:string,
      /**  Automatically void the legal number when the document is deleted  */  
   AutomaticVoiding:boolean,
      /**  The automatic voiding text  */  
   AutomaticVoidingText:string,
      /**  Use Change Log to track changes.  */  
   ChangeLog:boolean,
      /**  Created By  */  
   CreatedBy:string,
      /**  Created On  */  
   CreatedOn:string,
      /**  Changed By  */  
   ChangedBy:string,
      /**  Changed On  */  
   ChangedOn:string,
      /**  Stores the format defined to generate the Legal Number.  */  
   Format:string,
      /**  Separator is single character defined by user. It can be also used as Alternative Separator Character.  */  
   ConditionalSeparator:string,
      /**  Free text defined by user to be used in Legal Numbers.  */  
   FreeText:string,
      /**  Defines whether the Fiscal Year is displayed with 4  or 2 digits .  */  
   FiscalYearFormat:string,
      /**  Defines whether the FiscalPeriod is displayed with 1, 2, o 3 digits.  */  
   FiscalPeriodLength:number,
      /**  Defines if Day is displayed with leading zeros or not.  */  
   AddLeadingZero:boolean,
      /**  Determines if Automatic Generate Option is enabled.  */  
   EnableAutoGenerateOption:boolean,
      /**  Determines if Automatic Voiding Option is enabled.  */  
   EnableAutoVoidOption:boolean,
   FiscalCalDescription:string,
      /**  Number of folios that start to be voided.  */  
   FromFolio:string,
      /**  Inital sequence number from folio's number.  */  
   FromSeq:number,
   JournalCode:string,
   JrnlCodeJrnlDescription:string,
      /**  Foreign Key from LegalNumHistory Table used on Peru CSF as reference to run LegalNumberVoiding process  */  
   LegalNumHistForeignKey:string,
      /**  Field for Peru CSF, Legal Number to be voided  */  
   LegalNumHistLegalNumber:string,
   LegalNumTypeDesc:string,
      /**  This field will specify the working mode of the digital tax receipt functionality. Will have three possible values: "CFD", "CFDI" and "Disabled".  */  
   MXTaxRcptType:string,
      /**  The old default Prefix  */  
   OldDefaultPrefix:string,
      /**  Check Number on payment, this field is used for Peru CSF  */  
   PayCheckNum:number,
      /**  Document Check Amount on payment, this field is used for Peru CSF  */  
   PayDocCheckAmt:number,
      /**  Tax Amount on payment, this field is used for Peru CSF  */  
   PayDocTaxAmt:number,
      /**  Vendor ID on payment, this field is used for Peru CSF  */  
   PayVendorID:string,
      /**  Vendor Name on payment, this field is used for Peru CSF  */  
   PayVendorName:string,
      /**  Last number of folios to be voided.  */  
   ToFolio:string,
      /**  Last sequence number from folio's number.  */  
   ToSeq:number,
      /**  The Reason of the void Legal Number Folios.  */  
   VoidReason:string,
      /**  This field will be used to build Legal Number Folios.  */  
   VoidYear:number,
      /**  The list of automatic generation options  */  
   AutomaticGenerationList:string,
   LegalNumberSample:string,
      /**  Exclude Year in legal number format.  */  
   ExcludeYear:boolean,
      /**  Exclude period in legal number format.  */  
   ExcludePeriod:boolean,
   INShippingPortCode:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumCnfgTableset{
   LegalNumCnfg:Erp_Tablesets_LegalNumCnfgRow[],
   LegalNumDocType:Erp_Tablesets_LegalNumDocTypeRow[],
   LegalNumPrefix:Erp_Tablesets_LegalNumPrefixRow[],
   LegalNumSeqPrefix:Erp_Tablesets_LegalNumSeqPrefixRow[],
   LegalNumSeq:Erp_Tablesets_LegalNumSeqRow[],
   AvailableDocType:Erp_Tablesets_AvailableDocTypeRow[],
   AvailableLegalNumFormat:Erp_Tablesets_AvailableLegalNumFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LegalNumDocTypeRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The legal number identifier.  */  
   LegalNumberID:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumPrefixRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The legal number identifier.  */  
   LegalNumberID:string,
      /**  Prefix value for a legal number.  */  
   Prefix:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Valid values are "Required" and "System".  */  
   NumberOption:string,
      /**  Indicates if this is the default prefix for the legal number configuration.  */  
   CnfgDefault:boolean,
      /**  User ID  */  
   DcdUserID:string,
      /**  Warehouse used for the prefix  */  
   WarehouseCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OldPrefix:string,
      /**  if Prefix is empty then [Blank Prefix] otherwise Prefix name.  */  
   Description:string,
   BitFlag:number,
   plantName:string,
   WarehseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumSeqPrefixRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The transaction year the sequence applies to.  Based on a calendar year.  */  
   TransYear:number,
      /**  The transaction year suffix.  */  
   TransYearSuffix:string,
      /**  The prefix used for this sequence when generating a legal number.  */  
   Prefix:string,
      /**  The transaction period.  */  
   TransPeriod:number,
      /**  The next available sequence number.  */  
   NumberSeq:number,
      /**  The number of pre-printed forms available for the sequence.  */  
   AvailFolios:number,
      /**  The number of folios used for this sequence.  */  
   UsedFolios:number,
      /**  Start Sequence (Taiwan Localization field)  */  
   StartSequence:number,
      /**  End Sequence (Taiwan Localization field)  */  
   EndSequence:number,
      /**  Prefix used for the period. Available if TransPeriod > 0 (Taiwan Localization field)  */  
   PeriodPrefix:string,
      /**  Inactive (Taiwan Localization field)  */  
   Inactive:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGTableName  */  
   AGTableName:string,
      /**  AGInvoiceNum  */  
   AGInvoiceNum:number,
      /**  Approval Number (Mexico Localization field)  */  
   MXApprovalNum:number,
      /**  Approval Year (Mexico Localization field)  */  
   MXApprovalYear:number,
      /**  Expiration date for the sequence (Colombia Localization field)  */  
   COExpirationDate:string,
   CnfgDefault:boolean,
      /**  Used as reference to LegalNumPrefix, because the Prefix field has Period symbol in the end.  */  
   DefaultPrefix:string,
   LegalNumberID:string,
   Plant:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumSeqRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The transaction year the sequence applies to.  Based on a calendar year.  */  
   TransYear:number,
      /**  The transaction year suffix.  */  
   TransYearSuffix:string,
      /**  The prefix used for this sequence when generating a legal number.  */  
   Prefix:string,
      /**  The transaction period.  */  
   TransPeriod:number,
      /**  The next available sequence number.  */  
   NumberSeq:number,
      /**  The number of pre-printed forms available for the sequence.  */  
   AvailFolios:number,
      /**  The number of folios used for this sequence.  */  
   UsedFolios:number,
      /**  Start Sequence (Taiwan Localization field)  */  
   StartSequence:number,
      /**  End Sequence (Taiwan Localization field)  */  
   EndSequence:number,
      /**  Prefix used for the period. Available if TransPeriod > 0 (Taiwan Localization field)  */  
   PeriodPrefix:string,
      /**  Inactive (Taiwan Localization field)  */  
   Inactive:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGTableName  */  
   AGTableName:string,
      /**  AGInvoiceNum  */  
   AGInvoiceNum:number,
      /**  Approval Number (Mexico Localization field)  */  
   MXApprovalNum:number,
      /**  Approval Year (Mexico Localization field)  */  
   MXApprovalYear:number,
      /**  Expiration date for the sequence (Colombia Localization field)  */  
   COExpirationDate:string,
   DefaultPrefix:string,
   LegalNumberID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtLegalNumCnfgTableset{
   LegalNumCnfg:Erp_Tablesets_LegalNumCnfgRow[],
   LegalNumDocType:Erp_Tablesets_LegalNumDocTypeRow[],
   LegalNumPrefix:Erp_Tablesets_LegalNumPrefixRow[],
   LegalNumSeqPrefix:Erp_Tablesets_LegalNumSeqPrefixRow[],
   LegalNumSeq:Erp_Tablesets_LegalNumSeqRow[],
   AvailableDocType:Erp_Tablesets_AvailableDocTypeRow[],
   AvailableLegalNumFormat:Erp_Tablesets_AvailableLegalNumFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GenerateLegalNumberSample_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface GenerateLegalNumberSample_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param sSelectedFormatElemets
   */  
export interface GetAvailableFormatElementsExclExceedSeparators_input{
   sSelectedFormatElemets:string,
}

export interface GetAvailableFormatElementsExclExceedSeparators_output{
   returnObj:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface GetAvailableFormatElements_output{
   returnObj:Erp_Tablesets_LegalNumCnfgTableset[],
}

   /** Required : 
      @param legalNumberID
   */  
export interface GetByID_input{
   legalNumberID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_LegalNumCnfgTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_LegalNumCnfgTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_LegalNumCnfgTableset[],
}

   /** Required : 
      @param LegalNumber
   */  
export interface GetChangeLogDetails_input{
   LegalNumber:string,
}

export interface GetChangeLogDetails_output{
   returnObj:Erp_Tablesets_ChangeLogTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  Table Name  */  
   tableName:string,
      /**  Field Name  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

export interface GetLegalNumberTypeList_output{
parameters : {
      /**  output parameters  */  
   sLegalNumberTypeList:string,
}
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
   returnObj:Erp_Tablesets_LegalNumCnfgListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetMXTaxRcptType_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface GetNewLegalNumCnfg_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface GetNewLegalNumCnfg_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
      @param legalNumberID
   */  
export interface GetNewLegalNumDocType_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
   legalNumberID:string,
}

export interface GetNewLegalNumDocType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
      @param legalNumberID
      @param prefix
   */  
export interface GetNewLegalNumPrefix_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
   legalNumberID:string,
   prefix:string,
}

export interface GetNewLegalNumPrefix_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
      @param legalNumberID
      @param prefix
      @param plant
      @param transYear
      @param transYearSuffix
      @param transPeriod
   */  
export interface GetNewLegalNumSeqPrefix_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
   legalNumberID:string,
   prefix:string,
   plant:string,
   transYear:number,
   transYearSuffix:string,
   transPeriod:number,
}

export interface GetNewLegalNumSeqPrefix_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
      @param legalNumberID
      @param defaultPrefix
      @param transYear
      @param transYearSuffix
      @param transPeriod
   */  
export interface GetNewLegalNumSeq_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
   legalNumberID:string,
   defaultPrefix:string,
   transYear:number,
   transYearSuffix:string,
   transPeriod:number,
}

export interface GetNewLegalNumSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param whereClauseLegalNumCnfg
      @param whereClauseLegalNumDocType
      @param whereClauseLegalNumPrefix
      @param whereClauseLegalNumSeqPrefix
      @param whereClauseLegalNumSeq
      @param whereClauseAvailableDocType
      @param whereClauseAvailableLegalNumFormat
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseLegalNumCnfg:string,
   whereClauseLegalNumDocType:string,
   whereClauseLegalNumPrefix:string,
   whereClauseLegalNumSeqPrefix:string,
   whereClauseLegalNumSeq:string,
   whereClauseAvailableDocType:string,
   whereClauseAvailableLegalNumFormat:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_LegalNumCnfgTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipLegalNumberType
      @param ipLegalNumberID
   */  
export interface GetTranDocType_input{
      /**  The current legalNumberType Number  */  
   ipLegalNumberType:string,
      /**  The current legalNumberID Number  */  
   ipLegalNumberID:string,
}

export interface GetTranDocType_output{
   returnObj:Erp_Tablesets_LegalNumCnfgTableset[],
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
      @param sPreviousFormat
      @param sNewFormat
   */  
export interface OnChangeFormat_input{
      /**  Previous Legal Number format  */  
   sPreviousFormat:string,
      /**  New Legal Number format  */  
   sNewFormat:string,
}

export interface OnChangeFormat_output{
}

   /** Required : 
      @param ipGenSSCC
      @param ds
   */  
export interface OnChangeGenSSCC_input{
      /**  The current Generate SSCC value  */  
   ipGenSSCC:boolean,
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeGenSSCC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeOfGenerationOption_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeOfGenerationOption_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeOfGenerationType_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeOfGenerationType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param AutomaticVoiding
      @param ds
   */  
export interface OnChangeOfLegalNumCnfgAutomaticVoiding_input{
      /**  The Automatic Voiding Option  */  
   AutomaticVoiding:boolean,
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeOfLegalNumCnfgAutomaticVoiding_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ColumnName
      @param ds
   */  
export interface OnChangeOfLegalNumPrefix_input{
   ColumnName:string,
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeOfLegalNumPrefix_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeOfLegalNumSeqEndSequence_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeOfLegalNumSeqEndSequence_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeOfLegalNumSeqPrefixEndSequence_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeOfLegalNumSeqPrefixEndSequence_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeOfLegalNumSeqPrefixStartSequence_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeOfLegalNumSeqPrefixStartSequence_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeOfLegalNumSeqStartSequence_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeOfLegalNumSeqStartSequence_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ipLegalNumberType
      @param ds
   */  
export interface OnChangeOfLegalNumberType_input{
      /**  The current legalNumCnfg Number  */  
   ipLegalNumberType:string,
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeOfLegalNumberType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ipNumberOption
      @param ds
   */  
export interface OnChangeOfNumberOption_input{
      /**  The Number Option  */  
   ipNumberOption:string,
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeOfNumberOption_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeOfPrefixType_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface OnChangeOfPrefixType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ipLegalNumberID
      @param proposedDefaultPrefix
      @param ds
   */  
export interface ProcessPrefix_input{
      /**  The current legalNumCnfg Number  */  
   ipLegalNumberID:string,
      /**  Proposed default prefix  */  
   proposedDefaultPrefix:string,
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface ProcessPrefix_output{
parameters : {
      /**  output parameters  */  
   opMsgText:string,
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ipLegalNumberID
      @param ovPrefix
      @param plPrefix
      @param whPrefix
      @param usPrefix
      @param ds
   */  
export interface RemoveAltPrefix_input{
   ipLegalNumberID:string,
   ovPrefix:boolean,
   plPrefix:boolean,
   whPrefix:boolean,
   usPrefix:boolean,
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface RemoveAltPrefix_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ipLegalNumberID
      @param ds
   */  
export interface RemoveSequences_input{
      /**  Current legalNumCnfg Number  */  
   ipLegalNumberID:string,
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface RemoveSequences_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ResetTaxLegalNumber_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface ResetTaxLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface RetrievePaymentInfo_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface RetrievePaymentInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtLegalNumCnfgTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtLegalNumCnfgTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface VoidLegalNumCnfg_input{
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}

export interface VoidLegalNumCnfg_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LegalNumCnfgTableset[],
}
}

