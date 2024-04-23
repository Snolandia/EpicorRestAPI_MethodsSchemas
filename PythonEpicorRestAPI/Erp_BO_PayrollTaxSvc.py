import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PayrollTaxSvc
# Description: Payroll Tax Maintenance object
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PayrollTaxes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PayrollTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PayrollTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxMasRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes",headers=creds) as resp:
           return await resp.json()

async def post_PayrollTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PayrollTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxMasRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRTaxMasRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PayrollTaxes_Company_TaxTblID(Company, TaxTblID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PayrollTax item
   Description: Calls GetByID to retrieve the PayrollTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PayrollTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRTaxMasRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PayrollTaxes_Company_TaxTblID(Company, TaxTblID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PayrollTax for the service
   Description: Calls UpdateExt to update PayrollTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PayrollTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxMasRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PayrollTaxes_Company_TaxTblID(Company, TaxTblID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PayrollTax item
   Description: Call UpdateExt to delete PayrollTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PayrollTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PayrollTaxes_Company_TaxTblID_EntityGLCs(Company, TaxTblID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_PayrollTaxes_Company_TaxTblID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, TaxTblID, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PayrollTaxes_Company_TaxTblID_PRTaxDtls(Company, TaxTblID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PRTaxDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRTaxDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")/PRTaxDtls",headers=creds) as resp:
           return await resp.json()

async def get_PayrollTaxes_Company_TaxTblID_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear(Company, TaxTblID, FileStatus, TaxYear, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRTaxDtl item
   Description: Calls GetByID to retrieve the PRTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PayrollTaxes(" + Company + "," + TaxTblID + ")/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRTaxDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRTaxDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRTaxDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls",headers=creds) as resp:
           return await resp.json()

async def post_PRTaxDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRTaxDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear(Company, TaxTblID, FileStatus, TaxYear, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRTaxDtl item
   Description: Calls GetByID to retrieve the PRTaxDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear(Company, TaxTblID, FileStatus, TaxYear, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRTaxDtl for the service
   Description: Calls UpdateExt to update PRTaxDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRTaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear(Company, TaxTblID, FileStatus, TaxYear, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRTaxDtl item
   Description: Call UpdateExt to delete PRTaxDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRTaxDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxCrds(Company, TaxTblID, FileStatus, TaxYear, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PRTaxCrds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRTaxCrds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxCrdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxCrds",headers=creds) as resp:
           return await resp.json()

async def get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxCrds_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, FileStatus, TaxYear, TaxTblLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRTaxCrd item
   Description: Calls GetByID to retrieve the PRTaxCrd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxCrd1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRTaxCrdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxCrds(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxExps(Company, TaxTblID, FileStatus, TaxYear, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PRTaxExps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRTaxExps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxExpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxExps",headers=creds) as resp:
           return await resp.json()

async def get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxExps_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, FileStatus, TaxYear, TaxTblLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRTaxExp item
   Description: Calls GetByID to retrieve the PRTaxExp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxExp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRTaxExpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxExps(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxTbls(Company, TaxTblID, FileStatus, TaxYear, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PRTaxTbls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRTaxTbls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxTblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxTbls",headers=creds) as resp:
           return await resp.json()

async def get_PRTaxDtls_Company_TaxTblID_FileStatus_TaxYear_PRTaxTbls_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, FileStatus, TaxYear, TaxTblLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRTaxTbl item
   Description: Calls GetByID to retrieve the PRTaxTbl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxTbl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRTaxTblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxDtls(" + Company + "," + TaxTblID + "," + FileStatus + "," + TaxYear + ")/PRTaxTbls(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRTaxCrds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRTaxCrds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRTaxCrds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxCrdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxCrds",headers=creds) as resp:
           return await resp.json()

async def post_PRTaxCrds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRTaxCrds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxCrdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRTaxCrdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxCrds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRTaxCrds_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, TaxYear, FileStatus, TaxTblLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRTaxCrd item
   Description: Calls GetByID to retrieve the PRTaxCrd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxCrd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRTaxCrdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxCrds(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRTaxCrds_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, TaxYear, FileStatus, TaxTblLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRTaxCrd for the service
   Description: Calls UpdateExt to update PRTaxCrd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRTaxCrd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxCrdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxCrds(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRTaxCrds_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, TaxYear, FileStatus, TaxTblLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRTaxCrd item
   Description: Call UpdateExt to delete PRTaxCrd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRTaxCrd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxCrds(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRTaxExps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRTaxExps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRTaxExps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxExpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxExps",headers=creds) as resp:
           return await resp.json()

async def post_PRTaxExps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRTaxExps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxExpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRTaxExpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxExps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRTaxExps_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, TaxYear, FileStatus, TaxTblLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRTaxExp item
   Description: Calls GetByID to retrieve the PRTaxExp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxExp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRTaxExpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxExps(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRTaxExps_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, TaxYear, FileStatus, TaxTblLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRTaxExp for the service
   Description: Calls UpdateExt to update PRTaxExp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRTaxExp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxExpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxExps(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRTaxExps_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, TaxYear, FileStatus, TaxTblLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRTaxExp item
   Description: Call UpdateExt to delete PRTaxExp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRTaxExp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxExps(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_PRTaxTbls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PRTaxTbls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRTaxTbls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxTblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxTbls",headers=creds) as resp:
           return await resp.json()

async def post_PRTaxTbls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRTaxTbls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRTaxTblRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PRTaxTblRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxTbls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PRTaxTbls_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, TaxYear, FileStatus, TaxTblLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PRTaxTbl item
   Description: Calls GetByID to retrieve the PRTaxTbl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRTaxTbl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PRTaxTblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxTbls(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PRTaxTbls_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, TaxYear, FileStatus, TaxTblLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PRTaxTbl for the service
   Description: Calls UpdateExt to update PRTaxTbl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRTaxTbl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRTaxTblRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxTbls(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PRTaxTbls_Company_TaxTblID_TaxYear_FileStatus_TaxTblLine(Company, TaxTblID, TaxYear, FileStatus, TaxTblLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PRTaxTbl item
   Description: Call UpdateExt to delete PRTaxTbl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRTaxTbl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaxTblID: Desc: TaxTblID   Required: True   Allow empty value : True
      :param TaxYear: Desc: TaxYear   Required: True
      :param FileStatus: Desc: FileStatus   Required: True   Allow empty value : True
      :param TaxTblLine: Desc: TaxTblLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/PRTaxTbls(" + Company + "," + TaxTblID + "," + TaxYear + "," + FileStatus + "," + TaxTblLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRTaxMasListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePRTaxMas, whereClauseEntityGLC, whereClausePRTaxDtl, whereClausePRTaxCrd, whereClausePRTaxExp, whereClausePRTaxTbl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRTaxMas=" + whereClausePRTaxMas
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRTaxDtl=" + whereClausePRTaxDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRTaxCrd=" + whereClausePRTaxCrd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRTaxExp=" + whereClausePRTaxExp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePRTaxTbl=" + whereClausePRTaxTbl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(taxTblID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "taxTblID=" + taxTblID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckForDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForDetails
   Description: This method is to be called when leaving the PRTaxMas record by any means
(changing rows, new search, leaving the screen, etc.).  A PRTaxMas record must
have at least one PRTaxDtl record to be considered a valid PRTaxMas record.  If no
details exist for the PRTaxDtl, the user must either delete the PRTaxMas record or
add a detail record before being allowed to leave.
   OperationID: CheckForDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyDetails
   Description: This method copies a detail record for a specific TaxTblID, FileStatus and Year
to the specified new Year
   OperationID: CopyDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxMaster(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxMaster
   Description: This method creates a new PRTaxMas record after prompting for the TaxType.
Certain fields are initialized on create depending on which TaxType is being created.
This method replaces the standard GetNewPRTaxMas() method
   OperationID: GetNewTaxMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetFilingDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetFilingDescription
   Description: This method uses the PRTaxDtl.FileStatus field to determine the PRTaxDtl.FileStatusDesc
if there exists another PRTaxDtl with the same FileStatus for the same TaxTblID
   OperationID: SetFilingDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetFilingDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFilingDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetW2State(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetW2State
   Description: This method sets the W2State to the first 2 digits of the TaxTblId when the
taxType = "SIT" if the W2State is blank
   OperationID: SetW2State
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetW2State_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetW2State_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetNextOverAmount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetNextOverAmount
   Description: This method sets the OverAmount of the next taxTblLine record when NotOverAmount changes on previous line
   OperationID: SetNextOverAmount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetNextOverAmount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetNextOverAmount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRTaxMas(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRTaxMas
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxMas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxMas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxMas_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRTaxDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRTaxDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRTaxCrd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRTaxCrd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxCrd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxCrd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxCrd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRTaxExp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRTaxExp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxExp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxExp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxExp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPRTaxTbl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPRTaxTbl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRTaxTbl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPRTaxTbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRTaxTbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PayrollTaxSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxCrdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRTaxCrdRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRTaxDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxExpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRTaxExpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxMasListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRTaxMasListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxMasRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRTaxMasRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRTaxTblRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PRTaxTblRow] = obj["value"]
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxCrdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.TaxTblLine:int = obj["TaxTblLine"]
      """  An integer assigned by the system which is used to uniquely identify an individual table record within its related tax/filing status. This is assigned by reading last record and adding 1.  """  
      self.OverAmount:int = obj["OverAmount"]
      """   The lower amount range which the annualized range is compared to when selecting the proper table entry.
(See also NotOverAmount)  """  
      self.NotOverAmount:int = obj["NotOverAmount"]
      """   The higher amount range which the annualized range is compared to when selecting the proper table entry.  A  table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  """  
      self.CreditPercent:int = obj["CreditPercent"]
      """  Personal Tax Credit Percent.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      self.TaxYearFileStatusDesc:str = obj["TaxYearFileStatusDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.FileStatusDesc:str = obj["FileStatusDesc"]
      """  Description of this tax filing status master.  Ex: Married, Single.  """  
      self.TaxBasis:str = obj["TaxBasis"]
      """   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  """  
      self.TaxableWageLimit:int = obj["TaxableWageLimit"]
      """  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  """  
      self.StdDeductionMin:int = obj["StdDeductionMin"]
      """  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  """  
      self.StdDeductionMax:int = obj["StdDeductionMax"]
      """  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  """  
      self.StdDeductionPct:int = obj["StdDeductionPct"]
      """  Standard deduction percentage.  (See also StdDeductionMin, Max)  """  
      self.StdDeduction0:int = obj["StdDeduction0"]
      """  An annual deduction amount which some states use when personal exemptions = 0.  """  
      self.StdDeduction1:int = obj["StdDeduction1"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.StdDeduction2:int = obj["StdDeduction2"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.PersonalExAmt:int = obj["PersonalExAmt"]
      """  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  """  
      self.DependentExAmt:int = obj["DependentExAmt"]
      """  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  """  
      self.PersonalCrAmt:int = obj["PersonalCrAmt"]
      """  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.DependentCrAmt:int = obj["DependentCrAmt"]
      """  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.FITExPct:int = obj["FITExPct"]
      """  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  """  
      self.FITExMax:int = obj["FITExMax"]
      """  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  """  
      self.FICAExPct:int = obj["FICAExPct"]
      """  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  """  
      self.FICAExMax:int = obj["FICAExMax"]
      """   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  """  
      self.WeeklyLimit:int = obj["WeeklyLimit"]
      """  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  """  
      self.SupplementalPercent:int = obj["SupplementalPercent"]
      """   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  """  
      self.AddTaxPercent:int = obj["AddTaxPercent"]
      """  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  """  
      self.AddTaxAmount:int = obj["AddTaxAmount"]
      """  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  """  
      self.AddDeductionPercent:int = obj["AddDeductionPercent"]
      """  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  """  
      self.AddDeductionAmt1:int = obj["AddDeductionAmt1"]
      """  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  """  
      self.AddDeductionAmt2:int = obj["AddDeductionAmt2"]
      """  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  """  
      self.TaxableThreshold:int = obj["TaxableThreshold"]
      """  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  """  
      self.AboveThresholdPercent:int = obj["AboveThresholdPercent"]
      """  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  """  
      self.AboveThresholdAdditionalAmt:int = obj["AboveThresholdAdditionalAmt"]
      """  Added for OK payroll.  Additional tax amount for wages above threshold.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxExpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.TaxTblLine:int = obj["TaxTblLine"]
      """  An integer assigned by the system which is used to uniquely identify an individual table record within its related tax/filing status. This is assigned by reading last record and adding 1.  """  
      self.OverAmount:int = obj["OverAmount"]
      """   The lower amount range which the annualized range is compared to when selecting the proper table entry.
(See also NotOverAmount)  """  
      self.NotOverAmount:int = obj["NotOverAmount"]
      """   The higher amount range which the annualized range is compared to when selecting the proper table entry.  A  table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  """  
      self.ExemptionAmount:int = obj["ExemptionAmount"]
      """  Exemption amount.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      self.TaxYearFileStatusDesc:str = obj["TaxYearFileStatusDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxMasListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  A character set which is used as a component of the index to uniquely identify a tax master. Some tax types have system assigned values and some are assigned by the user. The system assigned values are as follows ( TaxType/TaxTblID); FIT/FED, FUTA/FUTA, SSEE/SSEE(Soc Sec Employee), SSER/SSER (Soc Sec Employer),  MDEE/MEDEE (Medicare Employee), MDER/MEDER (Medicare Employer).  """  
      self.TaxType:str = obj["TaxType"]
      """   Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SSEE" - Social Security employee paid, "SSER" - Social Security employer paid,  "MDEE" - Medicare employee paid, "MDER" - Medicare employer paid, "Locl" - Local.
Supplemental Percent is only allowed for FIT, SIT & Locl.  """  
      self.CalcOrder:int = obj["CalcOrder"]
      """   An internally used field to control the order in which taxes are calculated.  This is need because some taxes are based on a % of  FIT, SIT and others may have an exemption percent on FIT, SIT...
Values are assigned based on TaxType as follows:
FIT = 10, SSEE/SSER = 20, MDEE/MDER = 30, SIT = 4), Locl = 50, , FUTA = 80 and SUTA = 90  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.W2State:str = obj["W2State"]
      """  This State ID is used for printing on the W2 forms.  """  
      self.EmployerExp:bool = obj["EmployerExp"]
      """  Indicates if this tax is an expense to the employer. This is automatically set = Yes and disabled for FUTA & SUTA. The user would set this to yes for the employer's side of FICA.  """  
      self.TaxID:str = obj["TaxID"]
      """  This is the number by which your company is known to the taxing authority.  """  
      self.UnemploymentIns:bool = obj["UnemploymentIns"]
      """   Indicates whether or not this tax master represents unemployment insurance, such as FUTA or SUTA.  This is only used for reference purposes.
This is automatically set = Yes and disabled for FUTA & SUTA  """  
      self.RoundWithholdings:bool = obj["RoundWithholdings"]
      """  Some states require that withholding amounts per paycheck be rounded to the nearest dollar, this field will determine if withholding amounds will be rounded to the nearest dollar.  """  
      self.TaxIDRef:str = obj["TaxIDRef"]
      """  Tax ID Reference  """  
      self.StateTaxID:str = obj["StateTaxID"]
      """  State Tax ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxMasRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  A character set which is used as a component of the index to uniquely identify a tax master. Some tax types have system assigned values and some are assigned by the user. The system assigned values are as follows ( TaxType/TaxTblID); FIT/FED, FUTA/FUTA, SSEE/SSEE(Soc Sec Employee), SSER/SSER (Soc Sec Employer),  MDEE/MEDEE (Medicare Employee), MDER/MEDER (Medicare Employer).  """  
      self.TaxType:str = obj["TaxType"]
      """   Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SSEE" - Social Security employee paid, "SSER" - Social Security employer paid,  "MDEE" - Medicare employee paid, "MDER" - Medicare employer paid, "Locl" - Local.
Supplemental Percent is only allowed for FIT, SIT & Locl.  """  
      self.CalcOrder:int = obj["CalcOrder"]
      """   An internally used field to control the order in which taxes are calculated.  This is need because some taxes are based on a % of  FIT, SIT and others may have an exemption percent on FIT, SIT...
Values are assigned based on TaxType as follows:
FIT = 10, SSEE/SSER = 20, MDEE/MDER = 30, SIT = 4), Locl = 50, , FUTA = 80 and SUTA = 90  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.W2State:str = obj["W2State"]
      """  This State ID is used for printing on the W2 forms.  """  
      self.EmployerExp:bool = obj["EmployerExp"]
      """  Indicates if this tax is an expense to the employer. This is automatically set = Yes and disabled for FUTA & SUTA. The user would set this to yes for the employer's side of FICA.  """  
      self.TaxID:str = obj["TaxID"]
      """  This is the number by which your company is known to the taxing authority.  """  
      self.UnemploymentIns:bool = obj["UnemploymentIns"]
      """   Indicates whether or not this tax master represents unemployment insurance, such as FUTA or SUTA.  This is only used for reference purposes.
This is automatically set = Yes and disabled for FUTA & SUTA  """  
      self.RoundWithholdings:bool = obj["RoundWithholdings"]
      """  Some states require that withholding amounts per paycheck be rounded to the nearest dollar, this field will determine if withholding amounds will be rounded to the nearest dollar.  """  
      self.TaxIDRef:str = obj["TaxIDRef"]
      """  Tax ID Reference  """  
      self.StateTaxID:str = obj["StateTaxID"]
      """  State Tax ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxTblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.TaxTblLine:int = obj["TaxTblLine"]
      """  An integer assigned by the system which is used to uniquely identify an individual tax table record within its related tax/filing status. This is assigned by reading last record and adding 1.  """  
      self.OverAmount:int = obj["OverAmount"]
      """   The lower amount range which the annualized range is compared to when selecting the proper tax table entry.
(See also NotOverAmount)  """  
      self.NotOverAmount:int = obj["NotOverAmount"]
      """   The higher amount range which the annualized range is compared to when selecting the proper tax table entry.  A  tax table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  """  
      self.TaxAmount:int = obj["TaxAmount"]
      """   The Base tax amount for this tax table entry.  The actual tax is calculated as...
TaxAmount + ((AnnualizedWages - OverAmount) * OverTaxPct)).  """  
      self.OverTaxPct:int = obj["OverTaxPct"]
      """  The Tax percent at which the amount of the annualized wages are over the lower limit  (OverAmount) are taxed at.  """  
      self.WkTaxID1:int = obj["WkTaxID1"]
      """  Week Tax ID 1  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      self.TaxYearFileStatusDesc:str = obj["TaxYearFileStatusDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckForDetails_input:
   """ Required : 
   taxTblID
   """  
   def __init__(self, obj):
      self.taxTblID:str = obj["taxTblID"]
      """  Tax Table ID of the Tax Table record to validate  """  
      pass

class CheckForDetails_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CopyDetails_input:
   """ Required : 
   taxTblID
   fileStat
   fromYear
   toYear
   ds
   """  
   def __init__(self, obj):
      self.taxTblID:str = obj["taxTblID"]
      """  TaxTblID to copy from  """  
      self.fileStat:str = obj["fileStat"]
      """  Filing Status to copy from  """  
      self.fromYear:int = obj["fromYear"]
      """  Tax year to copy from  """  
      self.toYear:int = obj["toYear"]
      """  Tax year to copy to  """  
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

class CopyDetails_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   taxTblID
   """  
   def __init__(self, obj):
      self.taxTblID:str = obj["taxTblID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxCrdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.TaxTblLine:int = obj["TaxTblLine"]
      """  An integer assigned by the system which is used to uniquely identify an individual table record within its related tax/filing status. This is assigned by reading last record and adding 1.  """  
      self.OverAmount:int = obj["OverAmount"]
      """   The lower amount range which the annualized range is compared to when selecting the proper table entry.
(See also NotOverAmount)  """  
      self.NotOverAmount:int = obj["NotOverAmount"]
      """   The higher amount range which the annualized range is compared to when selecting the proper table entry.  A  table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  """  
      self.CreditPercent:int = obj["CreditPercent"]
      """  Personal Tax Credit Percent.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      self.TaxYearFileStatusDesc:str = obj["TaxYearFileStatusDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """  Tax year identifies the year in which this tax becomes effective. Note: The system uses the tax master which has a year equal or less than the check date when determining which tax master to use.  That means that the tax master does not have to be recreated every year if  there is no change from the previous year.  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.FileStatusDesc:str = obj["FileStatusDesc"]
      """  Description of this tax filing status master.  Ex: Married, Single.  """  
      self.TaxBasis:str = obj["TaxBasis"]
      """   Indicates the amount upon which the tax is calculated.  Valid values are G - % of Gross,  F - % of FIT,  S - % of SIT, or H - % of Hours. Note: The state of Oregon has a tax based on % of hours.
Note: This does not apply to supplemental tax calculations, they are always a percent of taxable gross wages.  """  
      self.TaxableWageLimit:int = obj["TaxableWageLimit"]
      """  The limit of annual wages after which taxes are no longer taken.  A wage limit is common in such taxes as Soc. Security, FUTA, SDI...  """  
      self.TaxPercent:int = obj["TaxPercent"]
      """  This percentage is used when the tax is not based on a graduated table.  That is, it's a fixed percentage regardless of wage amount.  """  
      self.StdDeductionMin:int = obj["StdDeductionMin"]
      """  The annual  minimum deduction amount.  This is the minimum annual deduction amount which is used when the deduction is a percent of wages within minimum and maximum limits.  """  
      self.StdDeductionMax:int = obj["StdDeductionMax"]
      """  The annual maximum deduction amount.  This is the maximum annual deduction amount which is used when the tax deduction is a percent of wages with minimum and maximum limits.  """  
      self.StdDeductionPct:int = obj["StdDeductionPct"]
      """  Standard deduction percentage.  (See also StdDeductionMin, Max)  """  
      self.StdDeduction0:int = obj["StdDeduction0"]
      """  An annual deduction amount which some states use when personal exemptions = 0.  """  
      self.StdDeduction1:int = obj["StdDeduction1"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.StdDeduction2:int = obj["StdDeduction2"]
      """  An annual deduction amount which some states use when personal exemptions = 1.  """  
      self.PersonalExAmt:int = obj["PersonalExAmt"]
      """  The annual exemption amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  """  
      self.DependentExAmt:int = obj["DependentExAmt"]
      """  The annual exemption amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.  """  
      self.PersonalCrAmt:int = obj["PersonalCrAmt"]
      """  The annual credit amount per personal exemption in this taxing locality.  This value is multiplied by the number of personal exemptions found in the employee master.  Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.DependentCrAmt:int = obj["DependentCrAmt"]
      """  The annual credit amount per dependent exemption in this taxing locality.  This value is multiplied by the number of dependent exemptions found in the employee master.
Credits differ from exemptions in that they are used to adjust tax amounts, not taxable wages.  """  
      self.FITExPct:int = obj["FITExPct"]
      """  The percentage of Federal Income Tax that is exempt from taxes for this taxing locality.  (See also FITExMax)  """  
      self.FITExMax:int = obj["FITExMax"]
      """  Maximum amount of FIT exemption for this tax locality. (see FITExPct).  """  
      self.FICAExPct:int = obj["FICAExPct"]
      """  The percentage of FICA that is tax exempt for this tax locality. Note: FICA include both Medicare & Soc. Security (See also FITExMax)  """  
      self.FICAExMax:int = obj["FICAExMax"]
      """   Maximum amount of FICA exemption for this locality. (see FICAExPct).
Note: FICA include both Medicare & Soc. Security.  """  
      self.WeeklyLimit:int = obj["WeeklyLimit"]
      """  The weekly limit that is withheld.  Ex: SDI in New York is .05% of weekly wages with a max of .60 cents per week.  """  
      self.SupplementalPercent:int = obj["SupplementalPercent"]
      """   The tax rate that is used for supplemental wages such as bonuses and commissions.
Note: Supplemental tax is always a percent of taxable gross.  """  
      self.AddTaxPercent:int = obj["AddTaxPercent"]
      """  This percentage is used for Oklahoma.  It is the additional tax percentage on gross wages over PRTaxDtl.AddTaxAmount.  """  
      self.AddTaxAmount:int = obj["AddTaxAmount"]
      """  This amount is used for Oklahoma.  It is the maximum wage amount before additional tax is calculated using field PRTaxDtl.AddTaxPercent.  """  
      self.AddDeductionPercent:int = obj["AddDeductionPercent"]
      """  This percent is used for Oklahoma.  It is the percentage used in calculating the additional deductions.  """  
      self.AddDeductionAmt1:int = obj["AddDeductionAmt1"]
      """  This amount is used for Oklahoma.  It is the deduction amount per exemption used in calculating the additional deductions.  """  
      self.AddDeductionAmt2:int = obj["AddDeductionAmt2"]
      """  This amount is used for Oklahoma.  It is the flat deduction amount used in calculating the additional deductions.  """  
      self.TaxableThreshold:int = obj["TaxableThreshold"]
      """  Added for OK payroll.  Wages above this threshold will recieve the Above Threshold Tax Percent.  """  
      self.AboveThresholdPercent:int = obj["AboveThresholdPercent"]
      """  Added for OK payroll.  Wages above the threshold amount will recieve this tax percent.  """  
      self.AboveThresholdAdditionalAmt:int = obj["AboveThresholdAdditionalAmt"]
      """  Added for OK payroll.  Additional tax amount for wages above threshold.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxExpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.TaxTblLine:int = obj["TaxTblLine"]
      """  An integer assigned by the system which is used to uniquely identify an individual table record within its related tax/filing status. This is assigned by reading last record and adding 1.  """  
      self.OverAmount:int = obj["OverAmount"]
      """   The lower amount range which the annualized range is compared to when selecting the proper table entry.
(See also NotOverAmount)  """  
      self.NotOverAmount:int = obj["NotOverAmount"]
      """   The higher amount range which the annualized range is compared to when selecting the proper table entry.  A  table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  """  
      self.ExemptionAmount:int = obj["ExemptionAmount"]
      """  Exemption amount.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      self.TaxYearFileStatusDesc:str = obj["TaxYearFileStatusDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxMasListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  A character set which is used as a component of the index to uniquely identify a tax master. Some tax types have system assigned values and some are assigned by the user. The system assigned values are as follows ( TaxType/TaxTblID); FIT/FED, FUTA/FUTA, SSEE/SSEE(Soc Sec Employee), SSER/SSER (Soc Sec Employer),  MDEE/MEDEE (Medicare Employee), MDER/MEDER (Medicare Employer).  """  
      self.TaxType:str = obj["TaxType"]
      """   Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SSEE" - Social Security employee paid, "SSER" - Social Security employer paid,  "MDEE" - Medicare employee paid, "MDER" - Medicare employer paid, "Locl" - Local.
Supplemental Percent is only allowed for FIT, SIT & Locl.  """  
      self.CalcOrder:int = obj["CalcOrder"]
      """   An internally used field to control the order in which taxes are calculated.  This is need because some taxes are based on a % of  FIT, SIT and others may have an exemption percent on FIT, SIT...
Values are assigned based on TaxType as follows:
FIT = 10, SSEE/SSER = 20, MDEE/MDER = 30, SIT = 4), Locl = 50, , FUTA = 80 and SUTA = 90  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.W2State:str = obj["W2State"]
      """  This State ID is used for printing on the W2 forms.  """  
      self.EmployerExp:bool = obj["EmployerExp"]
      """  Indicates if this tax is an expense to the employer. This is automatically set = Yes and disabled for FUTA & SUTA. The user would set this to yes for the employer's side of FICA.  """  
      self.TaxID:str = obj["TaxID"]
      """  This is the number by which your company is known to the taxing authority.  """  
      self.UnemploymentIns:bool = obj["UnemploymentIns"]
      """   Indicates whether or not this tax master represents unemployment insurance, such as FUTA or SUTA.  This is only used for reference purposes.
This is automatically set = Yes and disabled for FUTA & SUTA  """  
      self.RoundWithholdings:bool = obj["RoundWithholdings"]
      """  Some states require that withholding amounts per paycheck be rounded to the nearest dollar, this field will determine if withholding amounds will be rounded to the nearest dollar.  """  
      self.TaxIDRef:str = obj["TaxIDRef"]
      """  Tax ID Reference  """  
      self.StateTaxID:str = obj["StateTaxID"]
      """  State Tax ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxMasListTableset:
   def __init__(self, obj):
      self.PRTaxMasList:list[Erp_Tablesets_PRTaxMasListRow] = obj["PRTaxMasList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PRTaxMasRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  A character set which is used as a component of the index to uniquely identify a tax master. Some tax types have system assigned values and some are assigned by the user. The system assigned values are as follows ( TaxType/TaxTblID); FIT/FED, FUTA/FUTA, SSEE/SSEE(Soc Sec Employee), SSER/SSER (Soc Sec Employer),  MDEE/MEDEE (Medicare Employee), MDER/MEDER (Medicare Employer).  """  
      self.TaxType:str = obj["TaxType"]
      """   Identifies the type of tax table.  Valid values are "FIT" - Federal, "SIT" - State, "FUTA" - Federal Unemployment, "SUTA" - State Unemployment,  "SSEE" - Social Security employee paid, "SSER" - Social Security employer paid,  "MDEE" - Medicare employee paid, "MDER" - Medicare employer paid, "Locl" - Local.
Supplemental Percent is only allowed for FIT, SIT & Locl.  """  
      self.CalcOrder:int = obj["CalcOrder"]
      """   An internally used field to control the order in which taxes are calculated.  This is need because some taxes are based on a % of  FIT, SIT and others may have an exemption percent on FIT, SIT...
Values are assigned based on TaxType as follows:
FIT = 10, SSEE/SSER = 20, MDEE/MDER = 30, SIT = 4), Locl = 50, , FUTA = 80 and SUTA = 90  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.W2State:str = obj["W2State"]
      """  This State ID is used for printing on the W2 forms.  """  
      self.EmployerExp:bool = obj["EmployerExp"]
      """  Indicates if this tax is an expense to the employer. This is automatically set = Yes and disabled for FUTA & SUTA. The user would set this to yes for the employer's side of FICA.  """  
      self.TaxID:str = obj["TaxID"]
      """  This is the number by which your company is known to the taxing authority.  """  
      self.UnemploymentIns:bool = obj["UnemploymentIns"]
      """   Indicates whether or not this tax master represents unemployment insurance, such as FUTA or SUTA.  This is only used for reference purposes.
This is automatically set = Yes and disabled for FUTA & SUTA  """  
      self.RoundWithholdings:bool = obj["RoundWithholdings"]
      """  Some states require that withholding amounts per paycheck be rounded to the nearest dollar, this field will determine if withholding amounds will be rounded to the nearest dollar.  """  
      self.TaxIDRef:str = obj["TaxIDRef"]
      """  Tax ID Reference  """  
      self.StateTaxID:str = obj["StateTaxID"]
      """  State Tax ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PRTaxTblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  Tax Table ID  """  
      self.TaxYear:int = obj["TaxYear"]
      """   Mirror image of related PRTaxDtl.TaxYear.
(See PRTaxDtl.TaxYear)  """  
      self.FileStatus:str = obj["FileStatus"]
      """  A descriptive ID assigned by the user which is used to identify the filing status of this tax record.  Examples would be "S" - Single, M - Married,  H - Head of Household...Any characters are allowed but we suggest making them meaningful.  """  
      self.TaxTblLine:int = obj["TaxTblLine"]
      """  An integer assigned by the system which is used to uniquely identify an individual tax table record within its related tax/filing status. This is assigned by reading last record and adding 1.  """  
      self.OverAmount:int = obj["OverAmount"]
      """   The lower amount range which the annualized range is compared to when selecting the proper tax table entry.
(See also NotOverAmount)  """  
      self.NotOverAmount:int = obj["NotOverAmount"]
      """   The higher amount range which the annualized range is compared to when selecting the proper tax table entry.  A  tax table entry is selected when the annualized wage amount is greater than the OverAmount and Less than or equal to the corresponding NotOverAmount.
(See also OverAmount)  """  
      self.TaxAmount:int = obj["TaxAmount"]
      """   The Base tax amount for this tax table entry.  The actual tax is calculated as...
TaxAmount + ((AnnualizedWages - OverAmount) * OverTaxPct)).  """  
      self.OverTaxPct:int = obj["OverTaxPct"]
      """  The Tax percent at which the amount of the annualized wages are over the lower limit  (OverAmount) are taxed at.  """  
      self.WkTaxID1:int = obj["WkTaxID1"]
      """  Week Tax ID 1  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxTblIDDescription:str = obj["TaxTblIDDescription"]
      self.TaxYearFileStatusDesc:str = obj["TaxYearFileStatusDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PayrollTaxTableset:
   def __init__(self, obj):
      self.PRTaxMas:list[Erp_Tablesets_PRTaxMasRow] = obj["PRTaxMas"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.PRTaxDtl:list[Erp_Tablesets_PRTaxDtlRow] = obj["PRTaxDtl"]
      self.PRTaxCrd:list[Erp_Tablesets_PRTaxCrdRow] = obj["PRTaxCrd"]
      self.PRTaxExp:list[Erp_Tablesets_PRTaxExpRow] = obj["PRTaxExp"]
      self.PRTaxTbl:list[Erp_Tablesets_PRTaxTblRow] = obj["PRTaxTbl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPayrollTaxTableset:
   def __init__(self, obj):
      self.PRTaxMas:list[Erp_Tablesets_PRTaxMasRow] = obj["PRTaxMas"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.PRTaxDtl:list[Erp_Tablesets_PRTaxDtlRow] = obj["PRTaxDtl"]
      self.PRTaxCrd:list[Erp_Tablesets_PRTaxCrdRow] = obj["PRTaxCrd"]
      self.PRTaxExp:list[Erp_Tablesets_PRTaxExpRow] = obj["PRTaxExp"]
      self.PRTaxTbl:list[Erp_Tablesets_PRTaxTblRow] = obj["PRTaxTbl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   taxTblID
   """  
   def __init__(self, obj):
      self.taxTblID:str = obj["taxTblID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayrollTaxTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayrollTaxTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayrollTaxTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Tax Table ID  """  
      self.fieldName:str = obj["fieldName"]
      """  field name ID  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PRTaxMasListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRTaxCrd_input:
   """ Required : 
   ds
   taxTblID
   taxYear
   fileStatus
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      self.taxTblID:str = obj["taxTblID"]
      self.taxYear:int = obj["taxYear"]
      self.fileStatus:str = obj["fileStatus"]
      pass

class GetNewPRTaxCrd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRTaxDtl_input:
   """ Required : 
   ds
   taxTblID
   fileStatus
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      self.taxTblID:str = obj["taxTblID"]
      self.fileStatus:str = obj["fileStatus"]
      pass

class GetNewPRTaxDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRTaxExp_input:
   """ Required : 
   ds
   taxTblID
   taxYear
   fileStatus
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      self.taxTblID:str = obj["taxTblID"]
      self.taxYear:int = obj["taxYear"]
      self.fileStatus:str = obj["fileStatus"]
      pass

class GetNewPRTaxExp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRTaxMas_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

class GetNewPRTaxMas_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPRTaxTbl_input:
   """ Required : 
   ds
   taxTblID
   taxYear
   fileStatus
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      self.taxTblID:str = obj["taxTblID"]
      self.taxYear:int = obj["taxYear"]
      self.fileStatus:str = obj["fileStatus"]
      pass

class GetNewPRTaxTbl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxMaster_input:
   """ Required : 
   ds
   taxType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      self.taxType:str = obj["taxType"]
      """  Payroll Tax Master's Tax Type for new record  """  
      pass

class GetNewTaxMaster_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePRTaxMas
   whereClauseEntityGLC
   whereClausePRTaxDtl
   whereClausePRTaxCrd
   whereClausePRTaxExp
   whereClausePRTaxTbl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePRTaxMas:str = obj["whereClausePRTaxMas"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClausePRTaxDtl:str = obj["whereClausePRTaxDtl"]
      self.whereClausePRTaxCrd:str = obj["whereClausePRTaxCrd"]
      self.whereClausePRTaxExp:str = obj["whereClausePRTaxExp"]
      self.whereClausePRTaxTbl:str = obj["whereClausePRTaxTbl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PayrollTaxTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class SetFilingDescription_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

class SetFilingDescription_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetNextOverAmount_input:
   """ Required : 
   taxTblID
   fileStatus
   taxYear
   taxTblLine
   newNotOverAmt
   tableType
   ds
   """  
   def __init__(self, obj):
      self.taxTblID:str = obj["taxTblID"]
      """  current taxTblID being manipulated  """  
      self.fileStatus:str = obj["fileStatus"]
      """  current fileStatus bing manipulated  """  
      self.taxYear:int = obj["taxYear"]
      """  current taxYear being manipulated  """  
      self.taxTblLine:int = obj["taxTblLine"]
      """  current taxTblLine being manipulated  """  
      self.newNotOverAmt:int = obj["newNotOverAmt"]
      """  new NotOverAmount entered in UI  """  
      self.tableType:str = obj["tableType"]
      """  identifies which table is being manipulated  """  
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

class SetNextOverAmount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetW2State_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

class SetW2State_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPayrollTaxTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPayrollTaxTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PayrollTaxTableset] = obj["ds"]
      pass

      """  output parameters  """  

