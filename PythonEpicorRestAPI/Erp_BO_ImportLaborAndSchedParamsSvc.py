import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ImportLaborAndSchedParamsSvc
# Description: Business Object for the Import of Labor and Scheduling Parameters
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ImportLaborAndSchedParams(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ImportLaborAndSchedParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ImportLaborAndSchedParams
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImportGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams",headers=creds) as resp:
           return await resp.json()

async def post_ImportLaborAndSchedParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ImportLaborAndSchedParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ImportLaborAndSchedParams_Company_ImportID(Company, ImportID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ImportLaborAndSchedParam item
   Description: Calls GetByID to retrieve the ImportLaborAndSchedParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ImportLaborAndSchedParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ImportLaborAndSchedParams_Company_ImportID(Company, ImportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ImportLaborAndSchedParam for the service
   Description: Calls UpdateExt to update ImportLaborAndSchedParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ImportLaborAndSchedParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ImportLaborAndSchedParams_Company_ImportID(Company, ImportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ImportLaborAndSchedParam item
   Description: Call UpdateExt to delete ImportLaborAndSchedParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ImportLaborAndSchedParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportLaborAndSchedParams_Company_ImportID_LaborHedImports(Company, ImportID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborHedImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborHedImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborHedImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")/LaborHedImports",headers=creds) as resp:
           return await resp.json()

async def get_ImportLaborAndSchedParams_Company_ImportID_LaborHedImports_Company_ImportID_LaborHedSeq(Company, ImportID, LaborHedSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborHedImport item
   Description: Calls GetByID to retrieve the LaborHedImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborHedImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborHedImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ImportLaborAndSchedParams_Company_ImportID_SchedParamImports(Company, ImportID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SchedParamImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SchedParamImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SchedParamImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")/SchedParamImports",headers=creds) as resp:
           return await resp.json()

async def get_ImportLaborAndSchedParams_Company_ImportID_SchedParamImports_Company_ImportID_SchedParamSeq(Company, ImportID, SchedParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SchedParamImport item
   Description: Calls GetByID to retrieve the SchedParamImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SchedParamImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param SchedParamSeq: Desc: SchedParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SchedParamImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/ImportLaborAndSchedParams(" + Company + "," + ImportID + ")/SchedParamImports(" + Company + "," + ImportID + "," + SchedParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborHedImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborHedImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborHedImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborHedImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports",headers=creds) as resp:
           return await resp.json()

async def post_LaborHedImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborHedImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborHedImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborHedImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborHedImports_Company_ImportID_LaborHedSeq(Company, ImportID, LaborHedSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborHedImport item
   Description: Calls GetByID to retrieve the LaborHedImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborHedImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborHedImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborHedImports_Company_ImportID_LaborHedSeq(Company, ImportID, LaborHedSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborHedImport for the service
   Description: Calls UpdateExt to update LaborHedImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborHedImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborHedImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborHedImports_Company_ImportID_LaborHedSeq(Company, ImportID, LaborHedSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborHedImport item
   Description: Call UpdateExt to delete LaborHedImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborHedImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborHedImports_Company_ImportID_LaborHedSeq_LaborDtlImports(Company, ImportID, LaborHedSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborDtlImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborDtlImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")/LaborDtlImports",headers=creds) as resp:
           return await resp.json()

async def get_LaborHedImports_Company_ImportID_LaborHedSeq_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq(Company, ImportID, LaborHedSeq, LaborDtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtlImport item
   Description: Calls GetByID to retrieve the LaborDtlImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborHedImports(" + Company + "," + ImportID + "," + LaborHedSeq + ")/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborDtlImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtlImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports",headers=creds) as resp:
           return await resp.json()

async def post_LaborDtlImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtlImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborDtlImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq(Company, ImportID, LaborHedSeq, LaborDtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtlImport item
   Description: Calls GetByID to retrieve the LaborDtlImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq(Company, ImportID, LaborHedSeq, LaborDtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborDtlImport for the service
   Description: Calls UpdateExt to update LaborDtlImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtlImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq(Company, ImportID, LaborHedSeq, LaborDtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborDtlImport item
   Description: Call UpdateExt to delete LaborDtlImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtlImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_LaborEquipImports(Company, ImportID, LaborHedSeq, LaborDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborEquipImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborEquipImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborEquipImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborEquipImports",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_LaborEquipImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_EquipID(Company, ImportID, LaborHedSeq, LaborDtlSeq, EquipID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborEquipImport item
   Description: Calls GetByID to retrieve the LaborEquipImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborEquipImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborEquipImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborEquipImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_LaborPartImports(Company, ImportID, LaborHedSeq, LaborDtlSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborPartImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborPartImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborPartImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborPartImports",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum(Company, ImportID, LaborHedSeq, LaborDtlSeq, PartNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborPartImport item
   Description: Calls GetByID to retrieve the LaborPartImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborPartImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborPartImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborDtlImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborEquipImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborEquipImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborEquipImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborEquipImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborEquipImports",headers=creds) as resp:
           return await resp.json()

async def post_LaborEquipImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborEquipImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborEquipImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborEquipImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborEquipImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborEquipImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_EquipID(Company, ImportID, LaborHedSeq, LaborDtlSeq, EquipID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborEquipImport item
   Description: Calls GetByID to retrieve the LaborEquipImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborEquipImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborEquipImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborEquipImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborEquipImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_EquipID(Company, ImportID, LaborHedSeq, LaborDtlSeq, EquipID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborEquipImport for the service
   Description: Calls UpdateExt to update LaborEquipImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborEquipImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborEquipImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborEquipImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborEquipImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_EquipID(Company, ImportID, LaborHedSeq, LaborDtlSeq, EquipID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborEquipImport item
   Description: Call UpdateExt to delete LaborEquipImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborEquipImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborEquipImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + EquipID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborPartImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborPartImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborPartImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborPartImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports",headers=creds) as resp:
           return await resp.json()

async def post_LaborPartImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborPartImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborPartImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborPartImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum(Company, ImportID, LaborHedSeq, LaborDtlSeq, PartNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborPartImport item
   Description: Calls GetByID to retrieve the LaborPartImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborPartImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborPartImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum(Company, ImportID, LaborHedSeq, LaborDtlSeq, PartNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborPartImport for the service
   Description: Calls UpdateExt to update LaborPartImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborPartImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborPartImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum(Company, ImportID, LaborHedSeq, LaborDtlSeq, PartNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborPartImport item
   Description: Call UpdateExt to delete LaborPartImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborPartImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_LaborSerialNoImports(Company, ImportID, LaborHedSeq, LaborDtlSeq, PartNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborSerialNoImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborSerialNoImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborSerialNoImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")/LaborSerialNoImports",headers=creds) as resp:
           return await resp.json()

async def get_LaborPartImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_LaborSerialNoImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_SerialNumber(Company, ImportID, LaborHedSeq, LaborDtlSeq, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborSerialNoImport item
   Description: Calls GetByID to retrieve the LaborSerialNoImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborSerialNoImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborSerialNoImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborPartImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + ")/LaborSerialNoImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborSerialNoImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborSerialNoImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborSerialNoImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborSerialNoImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborSerialNoImports",headers=creds) as resp:
           return await resp.json()

async def post_LaborSerialNoImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborSerialNoImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborSerialNoImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborSerialNoImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborSerialNoImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborSerialNoImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_SerialNumber(Company, ImportID, LaborHedSeq, LaborDtlSeq, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborSerialNoImport item
   Description: Calls GetByID to retrieve the LaborSerialNoImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborSerialNoImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborSerialNoImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborSerialNoImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborSerialNoImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_SerialNumber(Company, ImportID, LaborHedSeq, LaborDtlSeq, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborSerialNoImport for the service
   Description: Calls UpdateExt to update LaborSerialNoImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborSerialNoImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborSerialNoImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborSerialNoImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborSerialNoImports_Company_ImportID_LaborHedSeq_LaborDtlSeq_PartNum_SerialNumber(Company, ImportID, LaborHedSeq, LaborDtlSeq, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborSerialNoImport item
   Description: Call UpdateExt to delete LaborSerialNoImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborSerialNoImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/LaborSerialNoImports(" + Company + "," + ImportID + "," + LaborHedSeq + "," + LaborDtlSeq + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SchedParamImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SchedParamImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SchedParamImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SchedParamImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/SchedParamImports",headers=creds) as resp:
           return await resp.json()

async def post_SchedParamImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SchedParamImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SchedParamImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SchedParamImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/SchedParamImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SchedParamImports_Company_ImportID_SchedParamSeq(Company, ImportID, SchedParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SchedParamImport item
   Description: Calls GetByID to retrieve the SchedParamImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SchedParamImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param SchedParamSeq: Desc: SchedParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SchedParamImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/SchedParamImports(" + Company + "," + ImportID + "," + SchedParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SchedParamImports_Company_ImportID_SchedParamSeq(Company, ImportID, SchedParamSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SchedParamImport for the service
   Description: Calls UpdateExt to update SchedParamImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SchedParamImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param SchedParamSeq: Desc: SchedParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SchedParamImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/SchedParamImports(" + Company + "," + ImportID + "," + SchedParamSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SchedParamImports_Company_ImportID_SchedParamSeq(Company, ImportID, SchedParamSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SchedParamImport item
   Description: Call UpdateExt to delete SchedParamImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SchedParamImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param SchedParamSeq: Desc: SchedParamSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/SchedParamImports(" + Company + "," + ImportID + "," + SchedParamSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImportGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseImportGrp, whereClauseLaborHedImport, whereClauseLaborDtlImport, whereClauseLaborEquipImport, whereClauseLaborPartImport, whereClauseLaborSerialNoImport, whereClauseSchedParamImport, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseImportGrp=" + whereClauseImportGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborHedImport=" + whereClauseLaborHedImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborDtlImport=" + whereClauseLaborDtlImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborEquipImport=" + whereClauseLaborEquipImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborPartImport=" + whereClauseLaborPartImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborSerialNoImport=" + whereClauseLaborSerialNoImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSchedParamImport=" + whereClauseSchedParamImport
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(importID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "importID=" + importID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_LaunchImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LaunchImport
   Description: Purpose: Launch the Import of Labor and Scheduling Parameters
   OperationID: LaunchImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LaunchImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LaunchImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LaunchImportWithSummarizing(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImportGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImportGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImportGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborHedImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborHedImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborHedImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborHedImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborHedImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtlImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtlImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtlImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborEquipImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborEquipImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborEquipImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborEquipImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborEquipImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborPartImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborPartImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborPartImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborPartImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborPartImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborSerialNoImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborSerialNoImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborSerialNoImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborSerialNoImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborSerialNoImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSchedParamImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSchedParamImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSchedParamImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSchedParamImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSchedParamImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ImportLaborAndSchedParamsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ImportGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ImportGrpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborDtlImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborEquipImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborEquipImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborHedImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborHedImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborPartImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborPartImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborSerialNoImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborSerialNoImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SchedParamImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SchedParamImportRow] = obj["value"]
      pass

class Erp_Tablesets_ImportGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.ImportType:str = obj["ImportType"]
      """  ImportType  """  
      self.ErrorFlag:bool = obj["ErrorFlag"]
      """  ErrorFlag  """  
      self.Status:str = obj["Status"]
      """  Status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DisplayImportID:str = obj["DisplayImportID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.ImportType:str = obj["ImportType"]
      """  ImportType  """  
      self.ErrorFlag:bool = obj["ErrorFlag"]
      """  ErrorFlag  """  
      self.Status:str = obj["Status"]
      """  Status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IntError:bool = obj["IntError"]
      self.DisplayImportID:str = obj["DisplayImportID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  EmployeeNum  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.LaborType:str = obj["LaborType"]
      """  LaborType  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """  LaborTypePseudo  """  
      self.ReWork:bool = obj["ReWork"]
      """  ReWork  """  
      self.ReworkReasonCode:str = obj["ReworkReasonCode"]
      """  ReworkReasonCode  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.JCDept:str = obj["JCDept"]
      """  JCDept  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  ResourceGrpID  """  
      self.OpCode:str = obj["OpCode"]
      """  OpCode  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  LaborHrs  """  
      self.BurdenHrs:int = obj["BurdenHrs"]
      """  BurdenHrs  """  
      self.LaborQty:int = obj["LaborQty"]
      """  LaborQty  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  ScrapQty  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  ScrapReasonCode  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  SetupPctComplete  """  
      self.Complete:bool = obj["Complete"]
      """  Complete  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  IndirectCode  """  
      self.LaborNote:str = obj["LaborNote"]
      """  LaborNote  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  LaborCollection  """  
      self.AppliedToSchedule:bool = obj["AppliedToSchedule"]
      """  AppliedToSchedule  """  
      self.ClockInMInute:int = obj["ClockInMInute"]
      """  ClockInMInute  """  
      self.ClockOutMinute:int = obj["ClockOutMinute"]
      """  ClockOutMinute  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  ClockInDate  """  
      self.ClockinTime:int = obj["ClockinTime"]
      """  ClockinTime  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """  ClockOutTime  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """  ActiveTrans  """  
      self.OverRidePayRate:int = obj["OverRidePayRate"]
      """  OverRidePayRate  """  
      self.LaborRate:int = obj["LaborRate"]
      """  LaborRate  """  
      self.BurdenRate:int = obj["BurdenRate"]
      """  BurdenRate  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  DspClockInTime  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  DspClockOutTime  """  
      self.ResourceID:str = obj["ResourceID"]
      """  ResourceID  """  
      self.OpComplete:bool = obj["OpComplete"]
      """  OpComplete  """  
      self.EarnedHrs:int = obj["EarnedHrs"]
      """  EarnedHrs  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  AddedOper  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  PayrollDate  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """  PostedToGL  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.JournalNum:int = obj["JournalNum"]
      """  JournalNum  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  GLTrans  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  InspectionPending  """  
      self.CallNum:int = obj["CallNum"]
      """  CallNum  """  
      self.CallLine:int = obj["CallLine"]
      """  CallLine  """  
      self.ServNum:int = obj["ServNum"]
      """  ServNum  """  
      self.ServCode:str = obj["ServCode"]
      """  ServCode  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  ResReasonCode  """  
      self.WipPosted:bool = obj["WipPosted"]
      """  WipPosted  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  DiscrepQty  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """  DiscrpRsnCode  """  
      self.ParentLaborDtlSeq:int = obj["ParentLaborDtlSeq"]
      """  ParentLaborDtlSeq  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  LaborEntryMethod  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.BFLaborReq:bool = obj["BFLaborReq"]
      """  BFLaborReq  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID  """  
      self.PhaseID:str = obj["PhaseID"]
      """  PhaseID  """  
      self.RoleCd:str = obj["RoleCd"]
      """  RoleCd  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  TimeTypCd  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  PBInvNum  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  TaskSetID  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  ApprovedDate  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  ClaimRef  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  QuickEntryCode  """  
      self.TimeStatus:str = obj["TimeStatus"]
      """  TimeStatus  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.CreateTime:int = obj["CreateTime"]
      """  CreateTime  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  ChangeTime  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  ActiveTaskID  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  LastTaskID  """  
      self.CreatedViaTEWeekView:bool = obj["CreatedViaTEWeekView"]
      """  CreatedViaTEWeekView  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  CurrentWFStageID  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  WFGroupID  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  WFComplete  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  ApprovalRequired  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  SubmittedBy  """  
      self.PBRateFrom:str = obj["PBRateFrom"]
      """  PBRateFrom  """  
      self.PBCurrencyCode:str = obj["PBCurrencyCode"]
      """  PBCurrencyCode  """  
      self.PBHours:int = obj["PBHours"]
      """  PBHours  """  
      self.PBChargeRate:int = obj["PBChargeRate"]
      """  PBChargeRate  """  
      self.PBChargeAmt:int = obj["PBChargeAmt"]
      """  PBChargeAmt  """  
      self.DocPBChargeRate:int = obj["DocPBChargeRate"]
      """  DocPBChargeRate  """  
      self.Rpt1PBChargeRate:int = obj["Rpt1PBChargeRate"]
      """  Rpt1PBChargeRate  """  
      self.Rpt2PBChargeRate:int = obj["Rpt2PBChargeRate"]
      """  Rpt2PBChargeRate  """  
      self.Rpt3PBChargeRate:int = obj["Rpt3PBChargeRate"]
      """  Rpt3PBChargeRate  """  
      self.DocPBChargeAmt:int = obj["DocPBChargeAmt"]
      """  DocPBChargeAmt  """  
      self.Rpt1PBChargeAmt:int = obj["Rpt1PBChargeAmt"]
      """  Rpt1PBChargeAmt  """  
      self.Rpt2PBChargeAmt:int = obj["Rpt2PBChargeAmt"]
      """  Rpt2PBChargeAmt  """  
      self.Rpt3PBChargeAmt:int = obj["Rpt3PBChargeAmt"]
      """  Rpt3PBChargeAmt  """  
      self.Shift:int = obj["Shift"]
      """  Shift  """  
      self.ActID:int = obj["ActID"]
      """  ActID  """  
      self.DtailID:int = obj["DtailID"]
      """  DtailID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  ProjProcessed  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  AsOfDate  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  AsOfSeq  """  
      self.JDFInputFiles:str = obj["JDFInputFiles"]
      """  JDFInputFiles  """  
      self.JDFNumberOfPages:str = obj["JDFNumberOfPages"]
      """  JDFNumberOfPages  """  
      self.BatchWasSaved:str = obj["BatchWasSaved"]
      """  BatchWasSaved  """  
      self.JDFCreatedByLink:bool = obj["JDFCreatedByLink"]
      """  JDFCreatedByLink  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchRequestMove:bool = obj["BatchRequestMove"]
      """  BatchRequestMove  """  
      self.BatchPrint:bool = obj["BatchPrint"]
      """  BatchPrint  """  
      self.BatchLaborHrs:int = obj["BatchLaborHrs"]
      """  BatchLaborHrs  """  
      self.BatchPctOfTotHrs:int = obj["BatchPctOfTotHrs"]
      """  BatchPctOfTotHrs  """  
      self.BatchQty:int = obj["BatchQty"]
      """  BatchQty  """  
      self.BatchTotalExpectedHrs:int = obj["BatchTotalExpectedHrs"]
      """  BatchTotalExpectedHrs  """  
      self.JDFOpCompleted:str = obj["JDFOpCompleted"]
      """  JDFOpCompleted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Downtime:bool = obj["Downtime"]
      """  Downtime  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.RefJobNum:str = obj["RefJobNum"]
      """  RefJobNum  """  
      self.RefAssemblySeq:int = obj["RefAssemblySeq"]
      """  RefAssemblySeq  """  
      self.RefOprSeq:int = obj["RefOprSeq"]
      """  RefOprSeq  """  
      self.FSComplete:bool = obj["FSComplete"]
      """  FSComplete  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """  TimeAutoSubmit  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.BillServiceRate:int = obj["BillServiceRate"]
      """  BillServiceRate  """  
      self.ExternalEmployeeSignedOut:bool = obj["ExternalEmployeeSignedOut"]
      """  Used with the summarize labor detail function to signal employee sign-out.  When set to true will signal the labor import process to close out the current active labor header and detail for that payroll date.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborEquipImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq  """  
      self.EquipID:str = obj["EquipID"]
      """  EquipID  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.Hours:int = obj["Hours"]
      """  Hours  """  
      self.Qty:int = obj["Qty"]
      """  Qty  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  CurrentMeter  """  
      self.MeterUOM:str = obj["MeterUOM"]
      """  MeterUOM  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborHedImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  EmployeeNum  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  PayrollDate  """  
      self.Shift:int = obj["Shift"]
      """  Shift  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  ClockInDate  """  
      self.ClockInTime:int = obj["ClockInTime"]
      """  ClockInTime  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  DspClockInTime  """  
      self.ActualClockInTime:int = obj["ActualClockInTime"]
      """  ActualClockInTime  """  
      self.ActualClockinDate:str = obj["ActualClockinDate"]
      """  ActualClockinDate  """  
      self.LunchStatus:str = obj["LunchStatus"]
      """  LunchStatus  """  
      self.ActLunchOutTime:int = obj["ActLunchOutTime"]
      """  ActLunchOutTime  """  
      self.LunchOutTime:int = obj["LunchOutTime"]
      """  LunchOutTime  """  
      self.ActLunchInTime:int = obj["ActLunchInTime"]
      """  ActLunchInTime  """  
      self.LunchInTime:int = obj["LunchInTime"]
      """  LunchInTime  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """  ClockOutTime  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  DspClockOutTime  """  
      self.ActualClockOutTime:int = obj["ActualClockOutTime"]
      """  ActualClockOutTime  """  
      self.PayHours:int = obj["PayHours"]
      """  PayHours  """  
      self.FeedPayroll:bool = obj["FeedPayroll"]
      """  FeedPayroll  """  
      self.TransferredToPayroll:bool = obj["TransferredToPayroll"]
      """  TransferredToPayroll  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  LaborCollection  """  
      self.TranSet:str = obj["TranSet"]
      """  TranSet  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """  ActiveTrans  """  
      self.ChkLink:str = obj["ChkLink"]
      """  ChkLink  """  
      self.BatchTotalHrsDisp:str = obj["BatchTotalHrsDisp"]
      """  BatchTotalHrsDisp  """  
      self.BatchHrsRemainDisp:str = obj["BatchHrsRemainDisp"]
      """  BatchHrsRemainDisp  """  
      self.BatchHrsRemainPctDisp:str = obj["BatchHrsRemainPctDisp"]
      """  BatchHrsRemainPctDisp  """  
      self.BatchSplitHrsMethod:str = obj["BatchSplitHrsMethod"]
      """  BatchSplitHrsMethod  """  
      self.BatchAssignTo:bool = obj["BatchAssignTo"]
      """  BatchAssignTo  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchStartHrs:str = obj["BatchStartHrs"]
      """  BatchStartHrs  """  
      self.BatchEndHrs:str = obj["BatchEndHrs"]
      """  BatchEndHrs  """  
      self.BatchTotalHrs:int = obj["BatchTotalHrs"]
      """  BatchTotalHrs  """  
      self.BatchHrsRemain:int = obj["BatchHrsRemain"]
      """  BatchHrsRemain  """  
      self.BatchHrsRemainPct:int = obj["BatchHrsRemainPct"]
      """  BatchHrsRemainPct  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.HCMPayHoursCalcType:str = obj["HCMPayHoursCalcType"]
      """  HCMPayHoursCalcType  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborPartImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.PartQty:int = obj["PartQty"]
      """  PartQty  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """  Discrepant Reason Code  """  
      self.DiscrpAttributeSetID:int = obj["DiscrpAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  Scrap Reason Code  """  
      self.ScrapAttributeSetID:int = obj["ScrapAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  """  
      self.NonConfTranID:int = obj["NonConfTranID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.LaborAttributeSetID:int = obj["LaborAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the PartQty  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborSerialNoImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.SNStatus:str = obj["SNStatus"]
      """  SNStatus  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SchedParamImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.SchedParamSeq:int = obj["SchedParamSeq"]
      """  SchedParamSeq  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  OpDtlSeq  """  
      self.StartDate:str = obj["StartDate"]
      """  StartDate  """  
      self.StartTime:int = obj["StartTime"]
      """  StartTime  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.EndTime:int = obj["EndTime"]
      """  EndTime  """  
      self.WhatIf:bool = obj["WhatIf"]
      """  WhatIf  """  
      self.Finite:bool = obj["Finite"]
      """  Finite  """  
      self.SchedTypeCode:str = obj["SchedTypeCode"]
      """  SchedTypeCode  """  
      self.OverrideMtlCon:bool = obj["OverrideMtlCon"]
      """  OverrideMtlCon  """  
      self.OverrideHistDateSetting:int = obj["OverrideHistDateSetting"]
      """  OverrideHistDateSetting  """  
      self.ScheduleDir:bool = obj["ScheduleDir"]
      """  ScheduleDir  """  
      self.SuppressExceptions:bool = obj["SuppressExceptions"]
      """  SuppressExceptions  """  
      self.AllocNum:int = obj["AllocNum"]
      """  AllocNum  """  
      self.ResourceID:str = obj["ResourceID"]
      """  ResourceID  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   importID
   """  
   def __init__(self, obj):
      self.importID:int = obj["importID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ImportGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.ImportType:str = obj["ImportType"]
      """  ImportType  """  
      self.ErrorFlag:bool = obj["ErrorFlag"]
      """  ErrorFlag  """  
      self.Status:str = obj["Status"]
      """  Status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DisplayImportID:str = obj["DisplayImportID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.ImportType:str = obj["ImportType"]
      """  ImportType  """  
      self.ErrorFlag:bool = obj["ErrorFlag"]
      """  ErrorFlag  """  
      self.Status:str = obj["Status"]
      """  Status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IntError:bool = obj["IntError"]
      self.DisplayImportID:str = obj["DisplayImportID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportLaborAndSchedParamsErrorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ImportID:int = obj["ImportID"]
      self.ErrorLogLineText:str = obj["ErrorLogLineText"]
      self.ErrorLogLineNum:int = obj["ErrorLogLineNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportLaborAndSchedParamsErrorTableset:
   def __init__(self, obj):
      self.ImportLaborAndSchedParamsError:list[Erp_Tablesets_ImportLaborAndSchedParamsErrorRow] = obj["ImportLaborAndSchedParamsError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ImportLaborAndSchedParamsListTableset:
   def __init__(self, obj):
      self.ImportGrpList:list[Erp_Tablesets_ImportGrpListRow] = obj["ImportGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ImportLaborAndSchedParamsTableset:
   def __init__(self, obj):
      self.ImportGrp:list[Erp_Tablesets_ImportGrpRow] = obj["ImportGrp"]
      self.LaborHedImport:list[Erp_Tablesets_LaborHedImportRow] = obj["LaborHedImport"]
      self.LaborDtlImport:list[Erp_Tablesets_LaborDtlImportRow] = obj["LaborDtlImport"]
      self.LaborEquipImport:list[Erp_Tablesets_LaborEquipImportRow] = obj["LaborEquipImport"]
      self.LaborPartImport:list[Erp_Tablesets_LaborPartImportRow] = obj["LaborPartImport"]
      self.LaborSerialNoImport:list[Erp_Tablesets_LaborSerialNoImportRow] = obj["LaborSerialNoImport"]
      self.SchedParamImport:list[Erp_Tablesets_SchedParamImportRow] = obj["SchedParamImport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LaborDtlImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  EmployeeNum  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.LaborType:str = obj["LaborType"]
      """  LaborType  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """  LaborTypePseudo  """  
      self.ReWork:bool = obj["ReWork"]
      """  ReWork  """  
      self.ReworkReasonCode:str = obj["ReworkReasonCode"]
      """  ReworkReasonCode  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.JCDept:str = obj["JCDept"]
      """  JCDept  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  ResourceGrpID  """  
      self.OpCode:str = obj["OpCode"]
      """  OpCode  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  LaborHrs  """  
      self.BurdenHrs:int = obj["BurdenHrs"]
      """  BurdenHrs  """  
      self.LaborQty:int = obj["LaborQty"]
      """  LaborQty  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  ScrapQty  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  ScrapReasonCode  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  SetupPctComplete  """  
      self.Complete:bool = obj["Complete"]
      """  Complete  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  IndirectCode  """  
      self.LaborNote:str = obj["LaborNote"]
      """  LaborNote  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  LaborCollection  """  
      self.AppliedToSchedule:bool = obj["AppliedToSchedule"]
      """  AppliedToSchedule  """  
      self.ClockInMInute:int = obj["ClockInMInute"]
      """  ClockInMInute  """  
      self.ClockOutMinute:int = obj["ClockOutMinute"]
      """  ClockOutMinute  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  ClockInDate  """  
      self.ClockinTime:int = obj["ClockinTime"]
      """  ClockinTime  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """  ClockOutTime  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """  ActiveTrans  """  
      self.OverRidePayRate:int = obj["OverRidePayRate"]
      """  OverRidePayRate  """  
      self.LaborRate:int = obj["LaborRate"]
      """  LaborRate  """  
      self.BurdenRate:int = obj["BurdenRate"]
      """  BurdenRate  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  DspClockInTime  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  DspClockOutTime  """  
      self.ResourceID:str = obj["ResourceID"]
      """  ResourceID  """  
      self.OpComplete:bool = obj["OpComplete"]
      """  OpComplete  """  
      self.EarnedHrs:int = obj["EarnedHrs"]
      """  EarnedHrs  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  AddedOper  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  PayrollDate  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """  PostedToGL  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.JournalNum:int = obj["JournalNum"]
      """  JournalNum  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  GLTrans  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  InspectionPending  """  
      self.CallNum:int = obj["CallNum"]
      """  CallNum  """  
      self.CallLine:int = obj["CallLine"]
      """  CallLine  """  
      self.ServNum:int = obj["ServNum"]
      """  ServNum  """  
      self.ServCode:str = obj["ServCode"]
      """  ServCode  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  ResReasonCode  """  
      self.WipPosted:bool = obj["WipPosted"]
      """  WipPosted  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  DiscrepQty  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """  DiscrpRsnCode  """  
      self.ParentLaborDtlSeq:int = obj["ParentLaborDtlSeq"]
      """  ParentLaborDtlSeq  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  LaborEntryMethod  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.BFLaborReq:bool = obj["BFLaborReq"]
      """  BFLaborReq  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID  """  
      self.PhaseID:str = obj["PhaseID"]
      """  PhaseID  """  
      self.RoleCd:str = obj["RoleCd"]
      """  RoleCd  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  TimeTypCd  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  PBInvNum  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  TaskSetID  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  ApprovedDate  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  ClaimRef  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  QuickEntryCode  """  
      self.TimeStatus:str = obj["TimeStatus"]
      """  TimeStatus  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.CreateTime:int = obj["CreateTime"]
      """  CreateTime  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  ChangeTime  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  ActiveTaskID  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  LastTaskID  """  
      self.CreatedViaTEWeekView:bool = obj["CreatedViaTEWeekView"]
      """  CreatedViaTEWeekView  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  CurrentWFStageID  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  WFGroupID  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  WFComplete  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  ApprovalRequired  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  SubmittedBy  """  
      self.PBRateFrom:str = obj["PBRateFrom"]
      """  PBRateFrom  """  
      self.PBCurrencyCode:str = obj["PBCurrencyCode"]
      """  PBCurrencyCode  """  
      self.PBHours:int = obj["PBHours"]
      """  PBHours  """  
      self.PBChargeRate:int = obj["PBChargeRate"]
      """  PBChargeRate  """  
      self.PBChargeAmt:int = obj["PBChargeAmt"]
      """  PBChargeAmt  """  
      self.DocPBChargeRate:int = obj["DocPBChargeRate"]
      """  DocPBChargeRate  """  
      self.Rpt1PBChargeRate:int = obj["Rpt1PBChargeRate"]
      """  Rpt1PBChargeRate  """  
      self.Rpt2PBChargeRate:int = obj["Rpt2PBChargeRate"]
      """  Rpt2PBChargeRate  """  
      self.Rpt3PBChargeRate:int = obj["Rpt3PBChargeRate"]
      """  Rpt3PBChargeRate  """  
      self.DocPBChargeAmt:int = obj["DocPBChargeAmt"]
      """  DocPBChargeAmt  """  
      self.Rpt1PBChargeAmt:int = obj["Rpt1PBChargeAmt"]
      """  Rpt1PBChargeAmt  """  
      self.Rpt2PBChargeAmt:int = obj["Rpt2PBChargeAmt"]
      """  Rpt2PBChargeAmt  """  
      self.Rpt3PBChargeAmt:int = obj["Rpt3PBChargeAmt"]
      """  Rpt3PBChargeAmt  """  
      self.Shift:int = obj["Shift"]
      """  Shift  """  
      self.ActID:int = obj["ActID"]
      """  ActID  """  
      self.DtailID:int = obj["DtailID"]
      """  DtailID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  ProjProcessed  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  AsOfDate  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  AsOfSeq  """  
      self.JDFInputFiles:str = obj["JDFInputFiles"]
      """  JDFInputFiles  """  
      self.JDFNumberOfPages:str = obj["JDFNumberOfPages"]
      """  JDFNumberOfPages  """  
      self.BatchWasSaved:str = obj["BatchWasSaved"]
      """  BatchWasSaved  """  
      self.JDFCreatedByLink:bool = obj["JDFCreatedByLink"]
      """  JDFCreatedByLink  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchRequestMove:bool = obj["BatchRequestMove"]
      """  BatchRequestMove  """  
      self.BatchPrint:bool = obj["BatchPrint"]
      """  BatchPrint  """  
      self.BatchLaborHrs:int = obj["BatchLaborHrs"]
      """  BatchLaborHrs  """  
      self.BatchPctOfTotHrs:int = obj["BatchPctOfTotHrs"]
      """  BatchPctOfTotHrs  """  
      self.BatchQty:int = obj["BatchQty"]
      """  BatchQty  """  
      self.BatchTotalExpectedHrs:int = obj["BatchTotalExpectedHrs"]
      """  BatchTotalExpectedHrs  """  
      self.JDFOpCompleted:str = obj["JDFOpCompleted"]
      """  JDFOpCompleted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Downtime:bool = obj["Downtime"]
      """  Downtime  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.RefJobNum:str = obj["RefJobNum"]
      """  RefJobNum  """  
      self.RefAssemblySeq:int = obj["RefAssemblySeq"]
      """  RefAssemblySeq  """  
      self.RefOprSeq:int = obj["RefOprSeq"]
      """  RefOprSeq  """  
      self.FSComplete:bool = obj["FSComplete"]
      """  FSComplete  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """  TimeAutoSubmit  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.BillServiceRate:int = obj["BillServiceRate"]
      """  BillServiceRate  """  
      self.ExternalEmployeeSignedOut:bool = obj["ExternalEmployeeSignedOut"]
      """  Used with the summarize labor detail function to signal employee sign-out.  When set to true will signal the labor import process to close out the current active labor header and detail for that payroll date.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborEquipImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq  """  
      self.EquipID:str = obj["EquipID"]
      """  EquipID  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.Hours:int = obj["Hours"]
      """  Hours  """  
      self.Qty:int = obj["Qty"]
      """  Qty  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  CurrentMeter  """  
      self.MeterUOM:str = obj["MeterUOM"]
      """  MeterUOM  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborHedImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  EmployeeNum  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  PayrollDate  """  
      self.Shift:int = obj["Shift"]
      """  Shift  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  ClockInDate  """  
      self.ClockInTime:int = obj["ClockInTime"]
      """  ClockInTime  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  DspClockInTime  """  
      self.ActualClockInTime:int = obj["ActualClockInTime"]
      """  ActualClockInTime  """  
      self.ActualClockinDate:str = obj["ActualClockinDate"]
      """  ActualClockinDate  """  
      self.LunchStatus:str = obj["LunchStatus"]
      """  LunchStatus  """  
      self.ActLunchOutTime:int = obj["ActLunchOutTime"]
      """  ActLunchOutTime  """  
      self.LunchOutTime:int = obj["LunchOutTime"]
      """  LunchOutTime  """  
      self.ActLunchInTime:int = obj["ActLunchInTime"]
      """  ActLunchInTime  """  
      self.LunchInTime:int = obj["LunchInTime"]
      """  LunchInTime  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """  ClockOutTime  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  DspClockOutTime  """  
      self.ActualClockOutTime:int = obj["ActualClockOutTime"]
      """  ActualClockOutTime  """  
      self.PayHours:int = obj["PayHours"]
      """  PayHours  """  
      self.FeedPayroll:bool = obj["FeedPayroll"]
      """  FeedPayroll  """  
      self.TransferredToPayroll:bool = obj["TransferredToPayroll"]
      """  TransferredToPayroll  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  LaborCollection  """  
      self.TranSet:str = obj["TranSet"]
      """  TranSet  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """  ActiveTrans  """  
      self.ChkLink:str = obj["ChkLink"]
      """  ChkLink  """  
      self.BatchTotalHrsDisp:str = obj["BatchTotalHrsDisp"]
      """  BatchTotalHrsDisp  """  
      self.BatchHrsRemainDisp:str = obj["BatchHrsRemainDisp"]
      """  BatchHrsRemainDisp  """  
      self.BatchHrsRemainPctDisp:str = obj["BatchHrsRemainPctDisp"]
      """  BatchHrsRemainPctDisp  """  
      self.BatchSplitHrsMethod:str = obj["BatchSplitHrsMethod"]
      """  BatchSplitHrsMethod  """  
      self.BatchAssignTo:bool = obj["BatchAssignTo"]
      """  BatchAssignTo  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchStartHrs:str = obj["BatchStartHrs"]
      """  BatchStartHrs  """  
      self.BatchEndHrs:str = obj["BatchEndHrs"]
      """  BatchEndHrs  """  
      self.BatchTotalHrs:int = obj["BatchTotalHrs"]
      """  BatchTotalHrs  """  
      self.BatchHrsRemain:int = obj["BatchHrsRemain"]
      """  BatchHrsRemain  """  
      self.BatchHrsRemainPct:int = obj["BatchHrsRemainPct"]
      """  BatchHrsRemainPct  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.HCMPayHoursCalcType:str = obj["HCMPayHoursCalcType"]
      """  HCMPayHoursCalcType  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborPartImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.PartQty:int = obj["PartQty"]
      """  PartQty  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """  Discrepant Reason Code  """  
      self.DiscrpAttributeSetID:int = obj["DiscrpAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """  Scrap Reason Code  """  
      self.ScrapAttributeSetID:int = obj["ScrapAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  """  
      self.NonConfTranID:int = obj["NonConfTranID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.LaborAttributeSetID:int = obj["LaborAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the PartQty  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborSerialNoImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.SNStatus:str = obj["SNStatus"]
      """  SNStatus  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SchedParamImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.SchedParamSeq:int = obj["SchedParamSeq"]
      """  SchedParamSeq  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  OpDtlSeq  """  
      self.StartDate:str = obj["StartDate"]
      """  StartDate  """  
      self.StartTime:int = obj["StartTime"]
      """  StartTime  """  
      self.EndDate:str = obj["EndDate"]
      """  EndDate  """  
      self.EndTime:int = obj["EndTime"]
      """  EndTime  """  
      self.WhatIf:bool = obj["WhatIf"]
      """  WhatIf  """  
      self.Finite:bool = obj["Finite"]
      """  Finite  """  
      self.SchedTypeCode:str = obj["SchedTypeCode"]
      """  SchedTypeCode  """  
      self.OverrideMtlCon:bool = obj["OverrideMtlCon"]
      """  OverrideMtlCon  """  
      self.OverrideHistDateSetting:int = obj["OverrideHistDateSetting"]
      """  OverrideHistDateSetting  """  
      self.ScheduleDir:bool = obj["ScheduleDir"]
      """  ScheduleDir  """  
      self.SuppressExceptions:bool = obj["SuppressExceptions"]
      """  SuppressExceptions  """  
      self.AllocNum:int = obj["AllocNum"]
      """  AllocNum  """  
      self.ResourceID:str = obj["ResourceID"]
      """  ResourceID  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorLog:str = obj["ErrorLog"]
      """  ErrorLog  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtImportLaborAndSchedParamsTableset:
   def __init__(self, obj):
      self.ImportGrp:list[Erp_Tablesets_ImportGrpRow] = obj["ImportGrp"]
      self.LaborHedImport:list[Erp_Tablesets_LaborHedImportRow] = obj["LaborHedImport"]
      self.LaborDtlImport:list[Erp_Tablesets_LaborDtlImportRow] = obj["LaborDtlImport"]
      self.LaborEquipImport:list[Erp_Tablesets_LaborEquipImportRow] = obj["LaborEquipImport"]
      self.LaborPartImport:list[Erp_Tablesets_LaborPartImportRow] = obj["LaborPartImport"]
      self.LaborSerialNoImport:list[Erp_Tablesets_LaborSerialNoImportRow] = obj["LaborSerialNoImport"]
      self.SchedParamImport:list[Erp_Tablesets_SchedParamImportRow] = obj["SchedParamImport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   importID
   """  
   def __init__(self, obj):
      self.importID:int = obj["importID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ImportLaborAndSchedParamsListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewImportGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      pass

class GetNewImportGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborDtlImport_input:
   """ Required : 
   ds
   importID
   laborHedSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      self.importID:int = obj["importID"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      pass

class GetNewLaborDtlImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborEquipImport_input:
   """ Required : 
   ds
   importID
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      self.importID:int = obj["importID"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetNewLaborEquipImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborHedImport_input:
   """ Required : 
   ds
   importID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      self.importID:int = obj["importID"]
      pass

class GetNewLaborHedImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborPartImport_input:
   """ Required : 
   ds
   importID
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      self.importID:int = obj["importID"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetNewLaborPartImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborSerialNoImport_input:
   """ Required : 
   ds
   importID
   laborHedSeq
   laborDtlSeq
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      self.importID:int = obj["importID"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewLaborSerialNoImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSchedParamImport_input:
   """ Required : 
   ds
   importID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      self.importID:int = obj["importID"]
      pass

class GetNewSchedParamImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseImportGrp
   whereClauseLaborHedImport
   whereClauseLaborDtlImport
   whereClauseLaborEquipImport
   whereClauseLaborPartImport
   whereClauseLaborSerialNoImport
   whereClauseSchedParamImport
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseImportGrp:str = obj["whereClauseImportGrp"]
      self.whereClauseLaborHedImport:str = obj["whereClauseLaborHedImport"]
      self.whereClauseLaborDtlImport:str = obj["whereClauseLaborDtlImport"]
      self.whereClauseLaborEquipImport:str = obj["whereClauseLaborEquipImport"]
      self.whereClauseLaborPartImport:str = obj["whereClauseLaborPartImport"]
      self.whereClauseLaborSerialNoImport:str = obj["whereClauseLaborSerialNoImport"]
      self.whereClauseSchedParamImport:str = obj["whereClauseSchedParamImport"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["returnObj"]
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

class LaunchImportWithSummarizing_input:
   """ Required : 
   ipImportID
   """  
   def __init__(self, obj):
      self.ipImportID:int = obj["ipImportID"]
      pass

class LaunchImportWithSummarizing_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImportLaborAndSchedParamsErrorTableset] = obj["returnObj"]
      pass

class LaunchImport_input:
   """ Required : 
   ipImportID
   """  
   def __init__(self, obj):
      self.ipImportID:int = obj["ipImportID"]
      pass

class LaunchImport_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ImportLaborAndSchedParamsErrorTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtImportLaborAndSchedParamsTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtImportLaborAndSchedParamsTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ImportLaborAndSchedParamsTableset] = obj["ds"]
      pass

      """  output parameters  """  

