import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GlRptMasSvc
# Description: Financial Report Designer business object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GlRptMas(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlRptMas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlRptMas
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlRptMasRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas",headers=creds) as resp:
           return await resp.json()

async def post_GlRptMas(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlRptMas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlRptMasRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlRptMasRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlRptMas_Company_ReportID(Company, ReportID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlRptMa item
   Description: Calls GetByID to retrieve the GlRptMa item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlRptMa
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlRptMasRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlRptMas_Company_ReportID(Company, ReportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlRptMa for the service
   Description: Calls UpdateExt to update GlRptMa. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlRptMa
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlRptMasRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlRptMas_Company_ReportID(Company, ReportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlRptMa item
   Description: Call UpdateExt to delete GlRptMa item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlRptMa
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlRptMas_Company_ReportID_GLRptColSets(Company, ReportID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLRptColSets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLRptColSets1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptColSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")/GLRptColSets",headers=creds) as resp:
           return await resp.json()

async def get_GlRptMas_Company_ReportID_GLRptColSets_Company_ReportID_ColSetSeq(Company, ReportID, ColSetSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLRptColSet item
   Description: Calls GetByID to retrieve the GLRptColSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptColSet1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param ColSetSeq: Desc: ColSetSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRptColSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlRptMas_Company_ReportID_GlRptRows(Company, ReportID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GlRptRows items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GlRptRows1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlRptRowRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")/GlRptRows",headers=creds) as resp:
           return await resp.json()

async def get_GlRptMas_Company_ReportID_GlRptRows_Company_ReportID_LineNum(Company, ReportID, LineNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlRptRow item
   Description: Calls GetByID to retrieve the GlRptRow item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlRptRow1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlRptRowRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLRptColSets(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLRptColSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLRptColSets
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptColSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets",headers=creds) as resp:
           return await resp.json()

async def post_GLRptColSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLRptColSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRptColSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLRptColSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLRptColSets_Company_ReportID_ColSetSeq(Company, ReportID, ColSetSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLRptColSet item
   Description: Calls GetByID to retrieve the GLRptColSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptColSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param ColSetSeq: Desc: ColSetSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRptColSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLRptColSets_Company_ReportID_ColSetSeq(Company, ReportID, ColSetSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLRptColSet for the service
   Description: Calls UpdateExt to update GLRptColSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLRptColSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param ColSetSeq: Desc: ColSetSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRptColSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLRptColSets_Company_ReportID_ColSetSeq(Company, ReportID, ColSetSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLRptColSet item
   Description: Call UpdateExt to delete GLRptColSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLRptColSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param ColSetSeq: Desc: ColSetSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLRptColSets_Company_ReportID_ColSetSeq_GLRptCols(Company, ReportID, ColSetSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLRptCols items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLRptCols1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param ColSetSeq: Desc: ColSetSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptColRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")/GLRptCols",headers=creds) as resp:
           return await resp.json()

async def get_GLRptColSets_Company_ReportID_ColSetSeq_GLRptCols_Company_ReportID_ColSetID_ColumnNum_SysRowID(Company, ReportID, ColSetSeq, ColSetID, ColumnNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLRptCol item
   Description: Calls GetByID to retrieve the GLRptCol item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptCol1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param ColSetSeq: Desc: ColSetSeq   Required: True
      :param ColSetID: Desc: ColSetID   Required: True   Allow empty value : True
      :param ColumnNum: Desc: ColumnNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRptColRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")/GLRptCols(" + Company + "," + ReportID + "," + ColSetID + "," + ColumnNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLRptCols(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLRptCols items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLRptCols
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptColRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptCols",headers=creds) as resp:
           return await resp.json()

async def post_GLRptCols(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLRptCols
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRptColRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLRptColRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptCols", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLRptCols_Company_ReportID_ColSetID_ColumnNum_SysRowID(Company, ReportID, ColSetID, ColumnNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLRptCol item
   Description: Calls GetByID to retrieve the GLRptCol item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptCol
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param ColSetID: Desc: ColSetID   Required: True   Allow empty value : True
      :param ColumnNum: Desc: ColumnNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRptColRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptCols(" + Company + "," + ReportID + "," + ColSetID + "," + ColumnNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLRptCols_Company_ReportID_ColSetID_ColumnNum_SysRowID(Company, ReportID, ColSetID, ColumnNum, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLRptCol for the service
   Description: Calls UpdateExt to update GLRptCol. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLRptCol
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param ColSetID: Desc: ColSetID   Required: True   Allow empty value : True
      :param ColumnNum: Desc: ColumnNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRptColRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptCols(" + Company + "," + ReportID + "," + ColSetID + "," + ColumnNum + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLRptCols_Company_ReportID_ColSetID_ColumnNum_SysRowID(Company, ReportID, ColSetID, ColumnNum, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLRptCol item
   Description: Call UpdateExt to delete GLRptCol item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLRptCol
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param ColSetID: Desc: ColSetID   Required: True   Allow empty value : True
      :param ColumnNum: Desc: ColumnNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptCols(" + Company + "," + ReportID + "," + ColSetID + "," + ColumnNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlRptRows(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlRptRows items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlRptRows
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlRptRowRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows",headers=creds) as resp:
           return await resp.json()

async def post_GlRptRows(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlRptRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlRptRowRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlRptRowRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlRptRows_Company_ReportID_LineNum(Company, ReportID, LineNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlRptRow item
   Description: Calls GetByID to retrieve the GlRptRow item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlRptRow
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlRptRowRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlRptRows_Company_ReportID_LineNum(Company, ReportID, LineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlRptRow for the service
   Description: Calls UpdateExt to update GlRptRow. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlRptRow
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlRptRowRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlRptRows_Company_ReportID_LineNum(Company, ReportID, LineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlRptRow item
   Description: Call UpdateExt to delete GlRptRow item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlRptRow
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlRptRows_Company_ReportID_LineNum_GLRptRowAccts(Company, ReportID, LineNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLRptRowAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLRptRowAccts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptRowAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")/GLRptRowAccts",headers=creds) as resp:
           return await resp.json()

async def get_GlRptRows_Company_ReportID_LineNum_GLRptRowAccts_Company_ReportID_LineNum_SeqNum(Company, ReportID, LineNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLRptRowAcct item
   Description: Calls GetByID to retrieve the GLRptRowAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptRowAcct1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRptRowAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")/GLRptRowAccts(" + Company + "," + ReportID + "," + LineNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLRptRowAccts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLRptRowAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLRptRowAccts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptRowAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptRowAccts",headers=creds) as resp:
           return await resp.json()

async def post_GLRptRowAccts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLRptRowAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRptRowAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLRptRowAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptRowAccts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLRptRowAccts_Company_ReportID_LineNum_SeqNum(Company, ReportID, LineNum, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLRptRowAcct item
   Description: Calls GetByID to retrieve the GLRptRowAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptRowAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLRptRowAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptRowAccts(" + Company + "," + ReportID + "," + LineNum + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLRptRowAccts_Company_ReportID_LineNum_SeqNum(Company, ReportID, LineNum, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLRptRowAcct for the service
   Description: Calls UpdateExt to update GLRptRowAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLRptRowAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRptRowAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptRowAccts(" + Company + "," + ReportID + "," + LineNum + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLRptRowAccts_Company_ReportID_LineNum_SeqNum(Company, ReportID, LineNum, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLRptRowAcct item
   Description: Call UpdateExt to delete GLRptRowAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLRptRowAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptRowAccts(" + Company + "," + ReportID + "," + LineNum + "," + SeqNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlRptMasListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGlRptMas, whereClauseGLRptColSet, whereClauseGLRptCol, whereClauseGlRptRow, whereClauseGLRptRowAcct, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGlRptMas=" + whereClauseGlRptMas
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLRptColSet=" + whereClauseGLRptColSet
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLRptCol=" + whereClauseGLRptCol
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGlRptRow=" + whereClauseGlRptRow
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLRptRowAcct=" + whereClauseGLRptRowAcct
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(reportID, epicorHeaders = None):
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
   params += "reportID=" + reportID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CategoryOrAccountsList(epicorHeaders = None):
   """  
   Summary: Invoke method CategoryOrAccountsList
   Description: Method to call to get the list for Category or Accounts option.  The list is
returned in code1`code desc1~code2`code desc2 format.
   OperationID: CategoryOrAccountsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CategoryOrAccountsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ChangeGLRptColColSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGLRptColColSetID
   Description: Method to call when the GLRptCol.ColSetID value changes.  The ColSetID can only
be changed for a new record.  This method will reassign the ColSetID of the
GLRptColSet record.
Prior to calling this method, the GLRptColSet record that exists for the GLRptCol
record needs to have the RowMod field set to 'U'.
   OperationID: ChangeGLRptColColSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGLRptColColSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptColColSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGLRptColColumnType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGLRptColColumnType
   Description: Method to call to reset values in a GLRptCol record when the column type changes.
   OperationID: ChangeGLRptColColumnType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGLRptColColumnType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptColColumnType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGLRptColIntervalType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGLRptColIntervalType
   Description: Method to call when the GLRptCol.IntervalType value changes.
   OperationID: ChangeGLRptColIntervalType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGLRptColIntervalType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptColIntervalType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGLRptMasBookID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGLRptMasBookID
   Description: Method to call when the GLRptMas.BookID value changes.
   OperationID: ChangeGLRptMasBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGLRptMasBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptMasBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGLRptRowCategoryOrAccounts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGLRptRowCategoryOrAccounts
   Description: Method to call to reset values in a GLRptRow record when the category or accounts
option changes.
Prior to calling this method, any GLRptRow subrecords that exist for the GLRptRow
record need to have the RowMod field set to 'U'.  The subtables for GLRptRow are:
GLRptRowAccounts, GLRptRowCharts, GLRptRowDepts, GLRptRowDivisions.
   OperationID: ChangeGLRptRowCategoryOrAccounts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGLRptRowCategoryOrAccounts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptRowCategoryOrAccounts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGLRptRowLineType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGLRptRowLineType
   Description: Method to call to reset values in a GLRptRow record when the line type changes.
Prior to calling this method, any GLRptRow subrecords that exist for the GLRptRow
record need to have the RowMod field set to 'U'.  The subtables for GLRptRow are:
GLRptRowAccounts, GLRptRowCharts, GLRptRowDepts, GLRptRowDivisions.
   OperationID: ChangeGLRptRowLineType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGLRptRowLineType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptRowLineType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ColumnTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method ColumnTypeList
   Description: Method to call to get the list of valid column types.  The list is returned in
code1`code desc1~code2`code desc2 format.
   OperationID: ColumnTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ColumnTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_DeleteColSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteColSet
   Description: Method to call to delete a column set for a financial report.  This method
delete the records in the column set and return the GlRptMas dataset.
   OperationID: DeleteColSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteColSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteColSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateFinancialReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateFinancialReport
   Description: Method to call to duplicate a financial report.  This method will return the
newly created records in the GlRptMas dataset.
   OperationID: DuplicateFinancialReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateFinancialReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateFinancialReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLRptRowAcctForType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLRptRowAcctForType
   Description: Creates a new GLRptRowAcct record based on type.
   OperationID: GetNewGLRptRowAcctForType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLRptRowAcctForType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRptRowAcctForType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LineTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method LineTypeList
   Description: Method to call to get the list of valid line types.  The list is returned in
code1`code desc1~code2`code desc2 format.
   OperationID: LineTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/LineTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_MoveGLRptColDown(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveGLRptColDown
   Description: Method to call to move a report column down within a column set.  This method
resequences the columns as appropriate and returns the updated dataset.
   OperationID: MoveGLRptColDown
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveGLRptColDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveGLRptColDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveGLRptColUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveGLRptColUp
   Description: Method to call to move a report column up within a column set.  This method
resequences the columns as appropriate and returns the updated dataset.
   OperationID: MoveGLRptColUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveGLRptColUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveGLRptColUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReportWizard(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReportWizard
   Description: Method to call to create a financial report using a wizard.  The wizard
will create a template report that be modified via the GlRptMas dataset.
   OperationID: ReportWizard
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReportWizard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportWizard_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReportWizardOptionsList(epicorHeaders = None):
   """  
   Summary: Invoke method ReportWizardOptionsList
   Description: Method to call to get the list of valid options for the report wizard.
The list is returned in code1`code desc1~code2`code desc2 format.
   OperationID: ReportWizardOptionsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportWizardOptionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SyntaxCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SyntaxCheck
   Description: Method to call to check the syntax of a report.  Syntax errors that occured
will be stored in datatable GLRptSyntaxErrors.
   OperationID: SyntaxCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SyntaxCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SyntaxCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SyntaxCheckForWeb(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SyntaxCheckForWeb
   Description: Method to call to check the syntax of a report.  Syntax errors that occured
will be stored in datatable GLRptSyntaxErrors.
Introduced for web use only.
   OperationID: SyntaxCheckForWeb
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SyntaxCheckForWeb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SyntaxCheckForWeb_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SyntaxCheckOptionsList(epicorHeaders = None):
   """  
   Summary: Invoke method SyntaxCheckOptionsList
   Description: Method to call to get the list of valid options for the syntax check.
The list is returned in code1`code desc1~code2`code desc2 format.
   OperationID: SyntaxCheckOptionsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SyntaxCheckOptionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateGLRptRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateGLRptRow
   Description: Method to call to validate that accounts or charts have been added to a row.
if applicable.  If accounts or charts are required, an exception will be thrown.
This method should be called prior to leaving the row for a different row.
   OperationID: ValidateGLRptRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateGLRptRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGLRptRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_YesNoDefaultList(epicorHeaders = None):
   """  
   Summary: Invoke method YesNoDefaultList
   Description: Method to call to get the list of valid entries for Yes/No/Default options.
The list is returned in code1`code desc1~code2`code desc2 format.
   OperationID: YesNoDefaultList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/YesNoDefaultList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ExportReportDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportReportDefinition
   Description: Export Report Definition to XML
   OperationID: ExportReportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportReportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportReportDefinition2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportReportDefinition2
   Description: Export Report Definition to XML, web make.
   OperationID: ExportReportDefinition2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportReportDefinition2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportDefinition2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateImportedReportDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateImportedReportDefinition
   Description: Validates imported (as an XML file) report definition.
   OperationID: ValidateImportedReportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateImportedReportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateImportedReportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportReportDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportReportDefinition
   Description: Import Report Definition from XML Data
   OperationID: ImportReportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportReportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportReportDefinition2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportReportDefinition2
   Description: Import Report Definition from XML Data, web make.
   OperationID: ImportReportDefinition2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportReportDefinition2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportDefinition2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlRptMas(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlRptMas
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlRptMas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlRptMas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlRptMas_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLRptCol(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLRptCol
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLRptCol
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLRptCol_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRptCol_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlRptRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlRptRow
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlRptRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlRptRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlRptRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLRptRowAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLRptRowAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLRptRowAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLRptRowAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRptRowAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLRptColRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLRptColSetRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptRowAcctRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLRptRowAcctRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptMasListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlRptMasListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptMasRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlRptMasRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptRowRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlRptRowRow] = obj["value"]
      pass

class Erp_Tablesets_GLRptColRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.ColSetID:str = obj["ColSetID"]
      """  Column Set Identifier used to establish different sets of columns for the same report specifications.  """  
      self.ColumnNum:int = obj["ColumnNum"]
      """  Indicates the number (position/order) of the column.  """  
      self.ShowAsPercent:bool = obj["ShowAsPercent"]
      """  This pertains to a  "Variance Column" only. Indicates if the variance is to be shown as a percentage or amount.  """  
      self.VarCol1:int = obj["VarCol1"]
      """  Used only for "Variance" columns.  Contains the "ColumnID" of the first column to be used to calculate the variance.  Variance is calculated as VarCol1 - VarCol2.  """  
      self.VarCol2:int = obj["VarCol2"]
      """  Used only for "Variance" columns.  Contains the "ColumnID" of the second column to be used to calculate the variance.  Variance is calculated as VarCol1 - VarCol2.  """  
      self.TotalCol1:int = obj["TotalCol1"]
      """  Used only for "Total" columns (ColumnType = "T").  Contains the "UniqueID" of the first column to be used to calculate the Total.  Column Totals are the sum of all "Data" columns beginning with TotalCol1 through TotalCol2.  """  
      self.TotalCol2:int = obj["TotalCol2"]
      """  Used only for "Total" columns (ColumnType = "T").  Contains the "UniqueID" of the  last column to be used to calculate the Total.  Column Totals are the sum of all "Data" columns beginning with TotalCol1 through TotalCol2.  """  
      self.ColumnTitle1:str = obj["ColumnTitle1"]
      """  Column title line one.  """  
      self.ColumnTitle2:str = obj["ColumnTitle2"]
      """  Column title line two.  """  
      self.ColumnType:str = obj["ColumnType"]
      """  A = Actuals,  B = Budget,  C = Comparative %, N = Acct #,  T = Text,   V = Variance, X = Crossfoot Total , U = statistical Unit of Measure, Q = Statistical Quantity , R - Report Category , D = Report Category Description  """  
      self.YearOffset:int = obj["YearOffset"]
      """  (Reporting year - YearOffset) = Fiscal Year of data in this column.  Ex: zero equal current year, 1 = prior year, etc...  """  
      self.PeriodOffset:int = obj["PeriodOffset"]
      """  (Reporting Period - PeriodOffset) = Fiscal Period of data in this column.  Ex: zero = current period, 1 = prior period, etc...  """  
      self.NumOfPeriods:int = obj["NumOfPeriods"]
      """   Number of fiscal period balances to be summarized into column.
Examples: Single Period = 01, Quarters = 3, Ytd = # of periods in fiscal year.  The system begins summarizing GL period balances starting at  "Given fiscal year - Year Offset", "Given fiscal period - period offset for the Number of periods indicated here.  If RollPeriods = No the summarization stops at period 1 of the "Given Fiscal Year - Year Offset", else it continues to the prior year.
NOTE: NumOfPeriods should not be > GLSyst.NumberofPeriods.  If it is logic will only summarize to the greater of the two.  """  
      self.RollingPeriods:bool = obj["RollingPeriods"]
      """  Indicates if the system should span fiscal year when summarizing the GL balances for the NumOfPeriods indicated.  In most cases this would be NO.  To produce a rolling number of periods the answer would be Yes.  """  
      self.TitleFont:str = obj["TitleFont"]
      """   Override FontName that is used for the Column Heading.
Default is GLRptMas.ReportFont  """  
      self.TitleFontSize:int = obj["TitleFontSize"]
      """  Override Font Size used for the column title. Default is Report.FontSize.  """  
      self.TitleUnderline:str = obj["TitleUnderline"]
      """   Override underline attribute for the column title.
Default is GLRptMas.ReportUnderline. 
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.TitleBold:str = obj["TitleBold"]
      """   Override Bold attribute for the column title.
Default is GLRptMas.ReportBold
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.TitleItalic:str = obj["TitleItalic"]
      """   Override Italic attribute for the column title.
Default is GLRptMas.ReporItalic. 
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.DataFont:str = obj["DataFont"]
      """  Override Font default that is used for the data in this column.  Default is GLRptMas.ReportFont  """  
      self.DataFontSize:int = obj["DataFontSize"]
      """  Override default Font Size used for data in this column. Default is GLRptMas.ReportFontSize.  """  
      self.DataUnderline:str = obj["DataUnderline"]
      """   Underline attribute for the data in this column.
Default is GLRptMas.ReportUnderline. 
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.DataBold:str = obj["DataBold"]
      """   Bold attribute for data in this column.
Default is GLRptMas.ReportBold
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.DataItalic:str = obj["DataItalic"]
      """   Italic attribute for data in this column.
Default is GLRptMas.ReporItalic. 
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.DailyAveBalance:bool = obj["DailyAveBalance"]
      """  Daily Average Balance option  """  
      self.NumOfDays:int = obj["NumOfDays"]
      """  Number of day balances to be summarized into column.  """  
      self.DaysOffset:int = obj["DaysOffset"]
      """  Days offset  """  
      self.IntervalType:str = obj["IntervalType"]
      """   Indicates if balances will be calculated by days or by periods.  Values are:
P - By Period
D - By Day  """  
      self.RollingDays:bool = obj["RollingDays"]
      """  Indicates if the system should span fiscal year when summarizing the GL balances for the NumOfDays indicated.  In most cases this would be NO.  To produce a rolling number of days the answer would be Yes.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OverrideBudgetCode:bool = obj["OverrideBudgetCode"]
      """  OverrideBudgetCode  """  
      self.BudgetCodeID:str = obj["BudgetCodeID"]
      """  BudgetCodeID  """  
      self.ColSetSeq:int = obj["ColSetSeq"]
      self.BitFlag:int = obj["BitFlag"]
      self.ReportIDDescription:str = obj["ReportIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRptColSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReportID:str = obj["ReportID"]
      self.ColSetID:str = obj["ColSetID"]
      self.ColumnTitle01:str = obj["ColumnTitle01"]
      self.ColumnTitle02:str = obj["ColumnTitle02"]
      self.ColumnTitle03:str = obj["ColumnTitle03"]
      self.ColumnTitle04:str = obj["ColumnTitle04"]
      self.ColumnTitle05:str = obj["ColumnTitle05"]
      self.ColumnTitle06:str = obj["ColumnTitle06"]
      self.ColumnTitle07:str = obj["ColumnTitle07"]
      self.ColumnTitle08:str = obj["ColumnTitle08"]
      self.ColumnTitle09:str = obj["ColumnTitle09"]
      self.ColumnTitle10:str = obj["ColumnTitle10"]
      self.ColumnTitle11:str = obj["ColumnTitle11"]
      self.ColumnTitle12:str = obj["ColumnTitle12"]
      self.ColumnTitle13:str = obj["ColumnTitle13"]
      self.ColumnTitle14:str = obj["ColumnTitle14"]
      self.ColumnTitle15:str = obj["ColumnTitle15"]
      self.ColumnTitle16:str = obj["ColumnTitle16"]
      self.ColumnTitle17:str = obj["ColumnTitle17"]
      self.ColumnTitle18:str = obj["ColumnTitle18"]
      self.ColumnTitle19:str = obj["ColumnTitle19"]
      self.ColumnTitle20:str = obj["ColumnTitle20"]
      self.ColSetSeq:int = obj["ColSetSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRptRowAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.LineNum:int = obj["LineNum"]
      """  Line number  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence number.   This along with ReportID and LineNum uniquely identifies the record.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  The segment number.  Blank if using a full account.  """  
      self.FromSegValue1:str = obj["FromSegValue1"]
      """  From Segement Value 1.  """  
      self.FromSegValue2:str = obj["FromSegValue2"]
      """  From Segement Value 2.  """  
      self.FromSegValue3:str = obj["FromSegValue3"]
      """  From Segement Value 3.  """  
      self.FromSegValue4:str = obj["FromSegValue4"]
      """  From Segement Value 4.  """  
      self.FromSegValue5:str = obj["FromSegValue5"]
      """  From Segement Value 5.  """  
      self.FromSegValue6:str = obj["FromSegValue6"]
      """  From Segement Value 6.  """  
      self.FromSegValue7:str = obj["FromSegValue7"]
      """  From Segement Value 7.  """  
      self.FromSegValue8:str = obj["FromSegValue8"]
      """  From Segement Value 8.  """  
      self.FromSegValue9:str = obj["FromSegValue9"]
      """  From Segement Value 9.  """  
      self.FromSegValue10:str = obj["FromSegValue10"]
      """  From Segement Value 10.  """  
      self.FromSegValue11:str = obj["FromSegValue11"]
      """  From Segement Value 11.  """  
      self.FromSegValue12:str = obj["FromSegValue12"]
      """  From Segement Value 12.  """  
      self.FromSegValue13:str = obj["FromSegValue13"]
      """  From Segement Value 13.  """  
      self.FromSegValue14:str = obj["FromSegValue14"]
      """  From Segement Value 14.  """  
      self.FromSegValue15:str = obj["FromSegValue15"]
      """  From Segement Value 15.  """  
      self.FromSegValue16:str = obj["FromSegValue16"]
      """  From Segement Value 16.  """  
      self.FromSegValue17:str = obj["FromSegValue17"]
      """  From Segement Value 17.  """  
      self.FromSegValue18:str = obj["FromSegValue18"]
      """  From Segement Value 18.  """  
      self.FromSegValue19:str = obj["FromSegValue19"]
      """  From Segement Value 19.  """  
      self.FromSegValue20:str = obj["FromSegValue20"]
      """  From Segement Value 20.  """  
      self.ToSegValue1:str = obj["ToSegValue1"]
      """  To Segement Value 1.  """  
      self.ToSegValue2:str = obj["ToSegValue2"]
      """  To Segement Value 2.  """  
      self.ToSegValue3:str = obj["ToSegValue3"]
      """  To Segement Value 3.  """  
      self.ToSegValue4:str = obj["ToSegValue4"]
      """  To Segement Value 4.  """  
      self.ToSegValue5:str = obj["ToSegValue5"]
      """  To Segement Value 5.  """  
      self.ToSegValue6:str = obj["ToSegValue6"]
      """  To Segement Value 6.  """  
      self.ToSegValue7:str = obj["ToSegValue7"]
      """  To Segement Value 7.  """  
      self.ToSegValue8:str = obj["ToSegValue8"]
      """  To Segement Value 8.  """  
      self.ToSegValue9:str = obj["ToSegValue9"]
      """  To Segement Value 9.  """  
      self.ToSegValue10:str = obj["ToSegValue10"]
      """  To Segement Value 10.  """  
      self.ToSegValue11:str = obj["ToSegValue11"]
      """  To Segement Value 11.  """  
      self.ToSegValue12:str = obj["ToSegValue12"]
      """  To Segement Value 12.  """  
      self.ToSegValue13:str = obj["ToSegValue13"]
      """  To Segement Value 13.  """  
      self.ToSegValue14:str = obj["ToSegValue14"]
      """  To Segement Value 14.  """  
      self.ToSegValue15:str = obj["ToSegValue15"]
      """  To Segement Value 15.  """  
      self.ToSegValue16:str = obj["ToSegValue16"]
      """  To Segement Value 16.  """  
      self.ToSegValue17:str = obj["ToSegValue17"]
      """  To Segement Value 17.  """  
      self.ToSegValue18:str = obj["ToSegValue18"]
      """  To Segement Value 18.  """  
      self.ToSegValue19:str = obj["ToSegValue19"]
      """  To Segement Value 19.  """  
      self.ToSegValue20:str = obj["ToSegValue20"]
      """  To Segement Value 20.  """  
      self.FromGLAccount:str = obj["FromGLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.ToGLAcct:str = obj["ToGLAcct"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.RowAcctType:str = obj["RowAcctType"]
      """   Indicates if this record contains a specific account or only a single segment.  Values are:
S - single segment
A - full account  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspFromSegValue:str = obj["DspFromSegValue"]
      """  From Segment Value entered by the user  """  
      self.DspToSegValue:str = obj["DspToSegValue"]
      """  The To Segment value entered by the user.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.FrmGLAccountAccountDesc:str = obj["FrmGLAccountAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlRptMasListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  ID that user assigns to uniquely identify a report definition.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Title that will be used for the report.  """  
      self.PctCalcTlLine:int = obj["PctCalcTlLine"]
      """  LineNum of the GLRptRow record which is to provide the denominator values in the Percent Of calculations.  """  
      self.HeadingFont:str = obj["HeadingFont"]
      """  FontName that is used for the Report Heading.  """  
      self.HeadingFontSize:int = obj["HeadingFontSize"]
      """  Font Size used for the Report Heading.  """  
      self.HeadingUnderline:bool = obj["HeadingUnderline"]
      """  Indicates if the Report Heading should be underlined.  """  
      self.HeadingBold:bool = obj["HeadingBold"]
      """  Indicates if the report heading lines should be Bold.  """  
      self.HeadingItalic:bool = obj["HeadingItalic"]
      """  Indicates if the report heading lines should be italic.  """  
      self.ReportFont:str = obj["ReportFont"]
      """  Default Font that is used for the Report. This may be overridden by specifications on the columns/Rows.TextFont  """  
      self.ReportFontSize:int = obj["ReportFontSize"]
      """  Default font size used for the report.  This may be overridden by specifications on the columns/rows.  """  
      self.ReportUnderline:bool = obj["ReportUnderline"]
      """  Default underline attribute for the report.   This may be overridden by specifications on the columns/rows.  """  
      self.ReportBold:bool = obj["ReportBold"]
      """  Default Bold attribute for the report.  This may be overridden by specifications on the columns/rows.  """  
      self.ReportItalic:bool = obj["ReportItalic"]
      """  Default Italic attribute for the report.   This may be overridden by specifications on the column.  """  
      self.AmountFactor:int = obj["AmountFactor"]
      """   The base 10 exponential factor for reported amounts and budgets.
Value 2 means 10 exp 3 = 1.000 resulting in the division of all amounts and budgets by 1.000.  """  
      self.BookID:str = obj["BookID"]
      """  Default Book Identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.BalanceLevel:str = obj["BalanceLevel"]
      """   The balance level for the report.  Values are:
D - Detail Account
S- Summary Account
N - Natural Account  """  
      self.BalanceFrequency:str = obj["BalanceFrequency"]
      """   Balance Frequence.  Values are:
P - Period balances
D - Daily balances  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableBookID:bool = obj["EnableBookID"]
      """  Indicates if the book id is enabled.  """  
      self.EnableCOACode:bool = obj["EnableCOACode"]
      """  Indicates if the COA Code is enabled.  """  
      self.COADescription:str = obj["COADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlRptMasRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  ID that user assigns to uniquely identify a report definition.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Title that will be used for the report.  """  
      self.PctCalcTlLine:int = obj["PctCalcTlLine"]
      """  LineNum of the GLRptRow record which is to provide the denominator values in the Percent Of calculations.  """  
      self.HeadingFont:str = obj["HeadingFont"]
      """  FontName that is used for the Report Heading.  """  
      self.HeadingFontSize:int = obj["HeadingFontSize"]
      """  Font Size used for the Report Heading.  """  
      self.HeadingUnderline:bool = obj["HeadingUnderline"]
      """  Indicates if the Report Heading should be underlined.  """  
      self.HeadingBold:bool = obj["HeadingBold"]
      """  Indicates if the report heading lines should be Bold.  """  
      self.HeadingItalic:bool = obj["HeadingItalic"]
      """  Indicates if the report heading lines should be italic.  """  
      self.ReportFont:str = obj["ReportFont"]
      """  Default Font that is used for the Report. This may be overridden by specifications on the columns/Rows.TextFont  """  
      self.ReportFontSize:int = obj["ReportFontSize"]
      """  Default font size used for the report.  This may be overridden by specifications on the columns/rows.  """  
      self.ReportUnderline:bool = obj["ReportUnderline"]
      """  Default underline attribute for the report.   This may be overridden by specifications on the columns/rows.  """  
      self.ReportBold:bool = obj["ReportBold"]
      """  Default Bold attribute for the report.  This may be overridden by specifications on the columns/rows.  """  
      self.ReportItalic:bool = obj["ReportItalic"]
      """  Default Italic attribute for the report.   This may be overridden by specifications on the column.  """  
      self.AmountFactor:int = obj["AmountFactor"]
      """   The base 10 exponential factor for reported amounts and budgets.
Value 2 means 10 exp 3 = 1.000 resulting in the division of all amounts and budgets by 1.000.  """  
      self.BookID:str = obj["BookID"]
      """  Default Book Identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.BalanceLevel:str = obj["BalanceLevel"]
      """   The balance level for the report.  Values are:
D - Detail Account
S- Summary Account
N - Natural Account  """  
      self.BalanceFrequency:str = obj["BalanceFrequency"]
      """   Balance Frequence.  Values are:
P - Period balances
D - Daily balances  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableBookID:bool = obj["EnableBookID"]
      """  Indicates if the book id is enabled.  """  
      self.EnableCOACode:bool = obj["EnableCOACode"]
      """  Indicates if the COA Code is enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlRptRowRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.LineNum:int = obj["LineNum"]
      """  Line number  """  
      self.LineType:str = obj["LineType"]
      """   H = Heading Line - Defines a Heading that is printed.
A = Account Details - Prints GL accounts in specified range
S = Summary - a summary of accounts in specified range.
R = Ratio between two rows. 
T = Total - prints a total line for specified total field.  """  
      self.Description:str = obj["Description"]
      """  For LineType H, S and T this description is used to identify the line. For LineType A (acct detail) it is only a reference; the actual description from the GLAcct is used when printing details.  """  
      self.TotalTo:str = obj["TotalTo"]
      """  Defines a field to which the values on this line are accumulated into.  """  
      self.PrintTotal:str = obj["PrintTotal"]
      """  Identifies the "TotalTo"  field that should be printed on this line. Pertains only to Total lines ( LineType = "T" ).  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates if the "signs" of the amounts for this line are to be flipped before they are printed.  """  
      self.NewPage:bool = obj["NewPage"]
      """  New Page flag  """  
      self.SkipBefore:int = obj["SkipBefore"]
      """  # of lines to skip before printing this line.  """  
      self.SkipAfter:int = obj["SkipAfter"]
      """  # of lines to skip after printing this line.  """  
      self.Indents:int = obj["Indents"]
      """  # of spaces that the line will be indented  """  
      self.ClearAfterPrint:bool = obj["ClearAfterPrint"]
      """   Resets the total field defined by "PrintTotal" to zero after printing.
Pertains only to Total lines ( LineType = T ).  """  
      self.TextFont:str = obj["TextFont"]
      """  Override Font that is used for the Text portion of a row. Default is either GLRptCol.DataFont or GLRptMas.ReportFont.  """  
      self.TextFontSize:int = obj["TextFontSize"]
      """  Override Text Font Size used for the Text portion of the row. Default is GLRptCol.DataFontSize or GLRptMas.ReportFontSize.  """  
      self.TextUnderline:str = obj["TextUnderline"]
      """   Underline attribute for the text portion of the line. Default is either GLRptCol.DataUnderLine or GLRptMas.ReportUnderline.
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.TextBold:str = obj["TextBold"]
      """   Bold attribute for the text portion of this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataBold or GLRptMas.ReportBold  """  
      self.TextItalic:str = obj["TextItalic"]
      """   Override Italic attribute for the text portion of this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataItalic or GLRptMas.ReporItalic.  """  
      self.DataFont:str = obj["DataFont"]
      """  Font that is used for ALL the data in this row.  Blank = use default. Default is either GLRptCol.DataFont/GLRptMas.ReportFont.  """  
      self.DataFontSize:int = obj["DataFontSize"]
      """   Override FontSize used for ALL DATA in this line. 0 = Use default.
Default is GLRptCol.DataFontSize/GLRptMas.ReportFontSize.  """  
      self.DataUnderline:str = obj["DataUnderline"]
      """   Underline attribute for ALL DATA in the line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataUnderLine/GLRptMas.ReportUnderline.  """  
      self.DataBold:str = obj["DataBold"]
      """   Bold attribute for ALL DATA on this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataBold/GLRptMas.ReportBold  """  
      self.DataItalic:str = obj["DataItalic"]
      """   Italic attribute for ALL DATA on this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataItalic/GLRptMas.ReporItalic.  """  
      self.RatioLine1:int = obj["RatioLine1"]
      """  The GLRptRow.LineNum that defines the values that are to be used the numerator in the ratio calculation. This only pertains to LineType = "R".  """  
      self.RatioLine2:int = obj["RatioLine2"]
      """  The GLRptRow.LineNum that defines the values that are to be used the denominator in the ratio calculation. This only pertains to LineType = "R".  """  
      self.Category:str = obj["Category"]
      """  Report Category  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text. Only for LineType="T"  """  
      self.ReverseReportCategory:str = obj["ReverseReportCategory"]
      """  ReverseReportCategory  """  
      self.CategoryOrAccounts:str = obj["CategoryOrAccounts"]
      self.COAActCatDescription:str = obj["COAActCatDescription"]
      self.IndentedDescription:str = obj["IndentedDescription"]
      self.PercentCalc:bool = obj["PercentCalc"]
      self.RptCOACode:str = obj["RptCOACode"]
      self.AllowNewAcct:bool = obj["AllowNewAcct"]
      """  Indicates of adding a new specific account is allowed.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ReportIDDescription:str = obj["ReportIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CategoryOrAccountsList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.CategoryOrAccountsList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeGLRptColColSetID_input:
   """ Required : 
   ProposedColSetID
   ds
   """  
   def __init__(self, obj):
      self.ProposedColSetID:str = obj["ProposedColSetID"]
      """  The proposed column set id  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class ChangeGLRptColColSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeGLRptColColumnType_input:
   """ Required : 
   ProposedColumnType
   ds
   """  
   def __init__(self, obj):
      self.ProposedColumnType:str = obj["ProposedColumnType"]
      """  The proposed column type  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class ChangeGLRptColColumnType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeGLRptColIntervalType_input:
   """ Required : 
   proposedIntervalType
   ds
   """  
   def __init__(self, obj):
      self.proposedIntervalType:str = obj["proposedIntervalType"]
      """  The proposed interval type value  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class ChangeGLRptColIntervalType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeGLRptMasBookID_input:
   """ Required : 
   proposedBookID
   ds
   """  
   def __init__(self, obj):
      self.proposedBookID:str = obj["proposedBookID"]
      """  The proposed book id  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class ChangeGLRptMasBookID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeGLRptRowCategoryOrAccounts_input:
   """ Required : 
   ProposedCategoryOrAccounts
   ds
   """  
   def __init__(self, obj):
      self.ProposedCategoryOrAccounts:str = obj["ProposedCategoryOrAccounts"]
      """  The proposed value  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class ChangeGLRptRowCategoryOrAccounts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeGLRptRowLineType_input:
   """ Required : 
   ProposedLineType
   ds
   """  
   def __init__(self, obj):
      self.ProposedLineType:str = obj["ProposedLineType"]
      """  The proposed column type  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class ChangeGLRptRowLineType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ColumnTypeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ColumnTypeList:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteColSet_input:
   """ Required : 
   DeleteFromReportID
   DeleteColSetID
   ds
   """  
   def __init__(self, obj):
      self.DeleteFromReportID:str = obj["DeleteFromReportID"]
      """  The report id to delete from  """  
      self.DeleteColSetID:str = obj["DeleteColSetID"]
      """  The column set to delete  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class DeleteColSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DuplicateFinancialReport_input:
   """ Required : 
   DuplicateFromReportID
   NewReportID
   NewReportDesc
   NewReportTitle
   ds
   """  
   def __init__(self, obj):
      self.DuplicateFromReportID:str = obj["DuplicateFromReportID"]
      """  The report id to duplicate from  """  
      self.NewReportID:str = obj["NewReportID"]
      """  The new report id  """  
      self.NewReportDesc:str = obj["NewReportDesc"]
      """  The new report description  """  
      self.NewReportTitle:str = obj["NewReportTitle"]
      """  The new report title  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class DuplicateFinancialReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_GLRptColRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.ColSetID:str = obj["ColSetID"]
      """  Column Set Identifier used to establish different sets of columns for the same report specifications.  """  
      self.ColumnNum:int = obj["ColumnNum"]
      """  Indicates the number (position/order) of the column.  """  
      self.ShowAsPercent:bool = obj["ShowAsPercent"]
      """  This pertains to a  "Variance Column" only. Indicates if the variance is to be shown as a percentage or amount.  """  
      self.VarCol1:int = obj["VarCol1"]
      """  Used only for "Variance" columns.  Contains the "ColumnID" of the first column to be used to calculate the variance.  Variance is calculated as VarCol1 - VarCol2.  """  
      self.VarCol2:int = obj["VarCol2"]
      """  Used only for "Variance" columns.  Contains the "ColumnID" of the second column to be used to calculate the variance.  Variance is calculated as VarCol1 - VarCol2.  """  
      self.TotalCol1:int = obj["TotalCol1"]
      """  Used only for "Total" columns (ColumnType = "T").  Contains the "UniqueID" of the first column to be used to calculate the Total.  Column Totals are the sum of all "Data" columns beginning with TotalCol1 through TotalCol2.  """  
      self.TotalCol2:int = obj["TotalCol2"]
      """  Used only for "Total" columns (ColumnType = "T").  Contains the "UniqueID" of the  last column to be used to calculate the Total.  Column Totals are the sum of all "Data" columns beginning with TotalCol1 through TotalCol2.  """  
      self.ColumnTitle1:str = obj["ColumnTitle1"]
      """  Column title line one.  """  
      self.ColumnTitle2:str = obj["ColumnTitle2"]
      """  Column title line two.  """  
      self.ColumnType:str = obj["ColumnType"]
      """  A = Actuals,  B = Budget,  C = Comparative %, N = Acct #,  T = Text,   V = Variance, X = Crossfoot Total , U = statistical Unit of Measure, Q = Statistical Quantity , R - Report Category , D = Report Category Description  """  
      self.YearOffset:int = obj["YearOffset"]
      """  (Reporting year - YearOffset) = Fiscal Year of data in this column.  Ex: zero equal current year, 1 = prior year, etc...  """  
      self.PeriodOffset:int = obj["PeriodOffset"]
      """  (Reporting Period - PeriodOffset) = Fiscal Period of data in this column.  Ex: zero = current period, 1 = prior period, etc...  """  
      self.NumOfPeriods:int = obj["NumOfPeriods"]
      """   Number of fiscal period balances to be summarized into column.
Examples: Single Period = 01, Quarters = 3, Ytd = # of periods in fiscal year.  The system begins summarizing GL period balances starting at  "Given fiscal year - Year Offset", "Given fiscal period - period offset for the Number of periods indicated here.  If RollPeriods = No the summarization stops at period 1 of the "Given Fiscal Year - Year Offset", else it continues to the prior year.
NOTE: NumOfPeriods should not be > GLSyst.NumberofPeriods.  If it is logic will only summarize to the greater of the two.  """  
      self.RollingPeriods:bool = obj["RollingPeriods"]
      """  Indicates if the system should span fiscal year when summarizing the GL balances for the NumOfPeriods indicated.  In most cases this would be NO.  To produce a rolling number of periods the answer would be Yes.  """  
      self.TitleFont:str = obj["TitleFont"]
      """   Override FontName that is used for the Column Heading.
Default is GLRptMas.ReportFont  """  
      self.TitleFontSize:int = obj["TitleFontSize"]
      """  Override Font Size used for the column title. Default is Report.FontSize.  """  
      self.TitleUnderline:str = obj["TitleUnderline"]
      """   Override underline attribute for the column title.
Default is GLRptMas.ReportUnderline. 
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.TitleBold:str = obj["TitleBold"]
      """   Override Bold attribute for the column title.
Default is GLRptMas.ReportBold
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.TitleItalic:str = obj["TitleItalic"]
      """   Override Italic attribute for the column title.
Default is GLRptMas.ReporItalic. 
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.DataFont:str = obj["DataFont"]
      """  Override Font default that is used for the data in this column.  Default is GLRptMas.ReportFont  """  
      self.DataFontSize:int = obj["DataFontSize"]
      """  Override default Font Size used for data in this column. Default is GLRptMas.ReportFontSize.  """  
      self.DataUnderline:str = obj["DataUnderline"]
      """   Underline attribute for the data in this column.
Default is GLRptMas.ReportUnderline. 
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.DataBold:str = obj["DataBold"]
      """   Bold attribute for data in this column.
Default is GLRptMas.ReportBold
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.DataItalic:str = obj["DataItalic"]
      """   Italic attribute for data in this column.
Default is GLRptMas.ReporItalic. 
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.DailyAveBalance:bool = obj["DailyAveBalance"]
      """  Daily Average Balance option  """  
      self.NumOfDays:int = obj["NumOfDays"]
      """  Number of day balances to be summarized into column.  """  
      self.DaysOffset:int = obj["DaysOffset"]
      """  Days offset  """  
      self.IntervalType:str = obj["IntervalType"]
      """   Indicates if balances will be calculated by days or by periods.  Values are:
P - By Period
D - By Day  """  
      self.RollingDays:bool = obj["RollingDays"]
      """  Indicates if the system should span fiscal year when summarizing the GL balances for the NumOfDays indicated.  In most cases this would be NO.  To produce a rolling number of days the answer would be Yes.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OverrideBudgetCode:bool = obj["OverrideBudgetCode"]
      """  OverrideBudgetCode  """  
      self.BudgetCodeID:str = obj["BudgetCodeID"]
      """  BudgetCodeID  """  
      self.ColSetSeq:int = obj["ColSetSeq"]
      self.BitFlag:int = obj["BitFlag"]
      self.ReportIDDescription:str = obj["ReportIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRptColSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReportID:str = obj["ReportID"]
      self.ColSetID:str = obj["ColSetID"]
      self.ColumnTitle01:str = obj["ColumnTitle01"]
      self.ColumnTitle02:str = obj["ColumnTitle02"]
      self.ColumnTitle03:str = obj["ColumnTitle03"]
      self.ColumnTitle04:str = obj["ColumnTitle04"]
      self.ColumnTitle05:str = obj["ColumnTitle05"]
      self.ColumnTitle06:str = obj["ColumnTitle06"]
      self.ColumnTitle07:str = obj["ColumnTitle07"]
      self.ColumnTitle08:str = obj["ColumnTitle08"]
      self.ColumnTitle09:str = obj["ColumnTitle09"]
      self.ColumnTitle10:str = obj["ColumnTitle10"]
      self.ColumnTitle11:str = obj["ColumnTitle11"]
      self.ColumnTitle12:str = obj["ColumnTitle12"]
      self.ColumnTitle13:str = obj["ColumnTitle13"]
      self.ColumnTitle14:str = obj["ColumnTitle14"]
      self.ColumnTitle15:str = obj["ColumnTitle15"]
      self.ColumnTitle16:str = obj["ColumnTitle16"]
      self.ColumnTitle17:str = obj["ColumnTitle17"]
      self.ColumnTitle18:str = obj["ColumnTitle18"]
      self.ColumnTitle19:str = obj["ColumnTitle19"]
      self.ColumnTitle20:str = obj["ColumnTitle20"]
      self.ColSetSeq:int = obj["ColSetSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRptRowAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.LineNum:int = obj["LineNum"]
      """  Line number  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence number.   This along with ReportID and LineNum uniquely identifies the record.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  The segment number.  Blank if using a full account.  """  
      self.FromSegValue1:str = obj["FromSegValue1"]
      """  From Segement Value 1.  """  
      self.FromSegValue2:str = obj["FromSegValue2"]
      """  From Segement Value 2.  """  
      self.FromSegValue3:str = obj["FromSegValue3"]
      """  From Segement Value 3.  """  
      self.FromSegValue4:str = obj["FromSegValue4"]
      """  From Segement Value 4.  """  
      self.FromSegValue5:str = obj["FromSegValue5"]
      """  From Segement Value 5.  """  
      self.FromSegValue6:str = obj["FromSegValue6"]
      """  From Segement Value 6.  """  
      self.FromSegValue7:str = obj["FromSegValue7"]
      """  From Segement Value 7.  """  
      self.FromSegValue8:str = obj["FromSegValue8"]
      """  From Segement Value 8.  """  
      self.FromSegValue9:str = obj["FromSegValue9"]
      """  From Segement Value 9.  """  
      self.FromSegValue10:str = obj["FromSegValue10"]
      """  From Segement Value 10.  """  
      self.FromSegValue11:str = obj["FromSegValue11"]
      """  From Segement Value 11.  """  
      self.FromSegValue12:str = obj["FromSegValue12"]
      """  From Segement Value 12.  """  
      self.FromSegValue13:str = obj["FromSegValue13"]
      """  From Segement Value 13.  """  
      self.FromSegValue14:str = obj["FromSegValue14"]
      """  From Segement Value 14.  """  
      self.FromSegValue15:str = obj["FromSegValue15"]
      """  From Segement Value 15.  """  
      self.FromSegValue16:str = obj["FromSegValue16"]
      """  From Segement Value 16.  """  
      self.FromSegValue17:str = obj["FromSegValue17"]
      """  From Segement Value 17.  """  
      self.FromSegValue18:str = obj["FromSegValue18"]
      """  From Segement Value 18.  """  
      self.FromSegValue19:str = obj["FromSegValue19"]
      """  From Segement Value 19.  """  
      self.FromSegValue20:str = obj["FromSegValue20"]
      """  From Segement Value 20.  """  
      self.ToSegValue1:str = obj["ToSegValue1"]
      """  To Segement Value 1.  """  
      self.ToSegValue2:str = obj["ToSegValue2"]
      """  To Segement Value 2.  """  
      self.ToSegValue3:str = obj["ToSegValue3"]
      """  To Segement Value 3.  """  
      self.ToSegValue4:str = obj["ToSegValue4"]
      """  To Segement Value 4.  """  
      self.ToSegValue5:str = obj["ToSegValue5"]
      """  To Segement Value 5.  """  
      self.ToSegValue6:str = obj["ToSegValue6"]
      """  To Segement Value 6.  """  
      self.ToSegValue7:str = obj["ToSegValue7"]
      """  To Segement Value 7.  """  
      self.ToSegValue8:str = obj["ToSegValue8"]
      """  To Segement Value 8.  """  
      self.ToSegValue9:str = obj["ToSegValue9"]
      """  To Segement Value 9.  """  
      self.ToSegValue10:str = obj["ToSegValue10"]
      """  To Segement Value 10.  """  
      self.ToSegValue11:str = obj["ToSegValue11"]
      """  To Segement Value 11.  """  
      self.ToSegValue12:str = obj["ToSegValue12"]
      """  To Segement Value 12.  """  
      self.ToSegValue13:str = obj["ToSegValue13"]
      """  To Segement Value 13.  """  
      self.ToSegValue14:str = obj["ToSegValue14"]
      """  To Segement Value 14.  """  
      self.ToSegValue15:str = obj["ToSegValue15"]
      """  To Segement Value 15.  """  
      self.ToSegValue16:str = obj["ToSegValue16"]
      """  To Segement Value 16.  """  
      self.ToSegValue17:str = obj["ToSegValue17"]
      """  To Segement Value 17.  """  
      self.ToSegValue18:str = obj["ToSegValue18"]
      """  To Segement Value 18.  """  
      self.ToSegValue19:str = obj["ToSegValue19"]
      """  To Segement Value 19.  """  
      self.ToSegValue20:str = obj["ToSegValue20"]
      """  To Segement Value 20.  """  
      self.FromGLAccount:str = obj["FromGLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.ToGLAcct:str = obj["ToGLAcct"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.RowAcctType:str = obj["RowAcctType"]
      """   Indicates if this record contains a specific account or only a single segment.  Values are:
S - single segment
A - full account  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspFromSegValue:str = obj["DspFromSegValue"]
      """  From Segment Value entered by the user  """  
      self.DspToSegValue:str = obj["DspToSegValue"]
      """  The To Segment value entered by the user.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COASegmentSegmentName:str = obj["COASegmentSegmentName"]
      self.FrmGLAccountAccountDesc:str = obj["FrmGLAccountAccountDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRptSyntaxErrorsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReportID:str = obj["ReportID"]
      self.DisplayAccount:str = obj["DisplayAccount"]
      self.SeqNum:int = obj["SeqNum"]
      self.ErrorType:int = obj["ErrorType"]
      self.ErrorDescription:str = obj["ErrorDescription"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLRptSyntaxErrorsTableset:
   def __init__(self, obj):
      self.GLRptSyntaxErrors:list[Erp_Tablesets_GLRptSyntaxErrorsRow] = obj["GLRptSyntaxErrors"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlRptMasListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  ID that user assigns to uniquely identify a report definition.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Title that will be used for the report.  """  
      self.PctCalcTlLine:int = obj["PctCalcTlLine"]
      """  LineNum of the GLRptRow record which is to provide the denominator values in the Percent Of calculations.  """  
      self.HeadingFont:str = obj["HeadingFont"]
      """  FontName that is used for the Report Heading.  """  
      self.HeadingFontSize:int = obj["HeadingFontSize"]
      """  Font Size used for the Report Heading.  """  
      self.HeadingUnderline:bool = obj["HeadingUnderline"]
      """  Indicates if the Report Heading should be underlined.  """  
      self.HeadingBold:bool = obj["HeadingBold"]
      """  Indicates if the report heading lines should be Bold.  """  
      self.HeadingItalic:bool = obj["HeadingItalic"]
      """  Indicates if the report heading lines should be italic.  """  
      self.ReportFont:str = obj["ReportFont"]
      """  Default Font that is used for the Report. This may be overridden by specifications on the columns/Rows.TextFont  """  
      self.ReportFontSize:int = obj["ReportFontSize"]
      """  Default font size used for the report.  This may be overridden by specifications on the columns/rows.  """  
      self.ReportUnderline:bool = obj["ReportUnderline"]
      """  Default underline attribute for the report.   This may be overridden by specifications on the columns/rows.  """  
      self.ReportBold:bool = obj["ReportBold"]
      """  Default Bold attribute for the report.  This may be overridden by specifications on the columns/rows.  """  
      self.ReportItalic:bool = obj["ReportItalic"]
      """  Default Italic attribute for the report.   This may be overridden by specifications on the column.  """  
      self.AmountFactor:int = obj["AmountFactor"]
      """   The base 10 exponential factor for reported amounts and budgets.
Value 2 means 10 exp 3 = 1.000 resulting in the division of all amounts and budgets by 1.000.  """  
      self.BookID:str = obj["BookID"]
      """  Default Book Identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.BalanceLevel:str = obj["BalanceLevel"]
      """   The balance level for the report.  Values are:
D - Detail Account
S- Summary Account
N - Natural Account  """  
      self.BalanceFrequency:str = obj["BalanceFrequency"]
      """   Balance Frequence.  Values are:
P - Period balances
D - Daily balances  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableBookID:bool = obj["EnableBookID"]
      """  Indicates if the book id is enabled.  """  
      self.EnableCOACode:bool = obj["EnableCOACode"]
      """  Indicates if the COA Code is enabled.  """  
      self.COADescription:str = obj["COADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.GLBookDescription:str = obj["GLBookDescription"]
      """  Descripiton of Book  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlRptMasListTableset:
   def __init__(self, obj):
      self.GlRptMasList:list[Erp_Tablesets_GlRptMasListRow] = obj["GlRptMasList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlRptMasRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  ID that user assigns to uniquely identify a report definition.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ReportTitle:str = obj["ReportTitle"]
      """  Title that will be used for the report.  """  
      self.PctCalcTlLine:int = obj["PctCalcTlLine"]
      """  LineNum of the GLRptRow record which is to provide the denominator values in the Percent Of calculations.  """  
      self.HeadingFont:str = obj["HeadingFont"]
      """  FontName that is used for the Report Heading.  """  
      self.HeadingFontSize:int = obj["HeadingFontSize"]
      """  Font Size used for the Report Heading.  """  
      self.HeadingUnderline:bool = obj["HeadingUnderline"]
      """  Indicates if the Report Heading should be underlined.  """  
      self.HeadingBold:bool = obj["HeadingBold"]
      """  Indicates if the report heading lines should be Bold.  """  
      self.HeadingItalic:bool = obj["HeadingItalic"]
      """  Indicates if the report heading lines should be italic.  """  
      self.ReportFont:str = obj["ReportFont"]
      """  Default Font that is used for the Report. This may be overridden by specifications on the columns/Rows.TextFont  """  
      self.ReportFontSize:int = obj["ReportFontSize"]
      """  Default font size used for the report.  This may be overridden by specifications on the columns/rows.  """  
      self.ReportUnderline:bool = obj["ReportUnderline"]
      """  Default underline attribute for the report.   This may be overridden by specifications on the columns/rows.  """  
      self.ReportBold:bool = obj["ReportBold"]
      """  Default Bold attribute for the report.  This may be overridden by specifications on the columns/rows.  """  
      self.ReportItalic:bool = obj["ReportItalic"]
      """  Default Italic attribute for the report.   This may be overridden by specifications on the column.  """  
      self.AmountFactor:int = obj["AmountFactor"]
      """   The base 10 exponential factor for reported amounts and budgets.
Value 2 means 10 exp 3 = 1.000 resulting in the division of all amounts and budgets by 1.000.  """  
      self.BookID:str = obj["BookID"]
      """  Default Book Identifier  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account Code  """  
      self.BalanceLevel:str = obj["BalanceLevel"]
      """   The balance level for the report.  Values are:
D - Detail Account
S- Summary Account
N - Natural Account  """  
      self.BalanceFrequency:str = obj["BalanceFrequency"]
      """   Balance Frequence.  Values are:
P - Period balances
D - Daily balances  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableBookID:bool = obj["EnableBookID"]
      """  Indicates if the book id is enabled.  """  
      self.EnableCOACode:bool = obj["EnableCOACode"]
      """  Indicates if the COA Code is enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlRptMasTableset:
   def __init__(self, obj):
      self.GlRptMas:list[Erp_Tablesets_GlRptMasRow] = obj["GlRptMas"]
      self.GLRptColSet:list[Erp_Tablesets_GLRptColSetRow] = obj["GLRptColSet"]
      self.GLRptCol:list[Erp_Tablesets_GLRptColRow] = obj["GLRptCol"]
      self.GlRptRow:list[Erp_Tablesets_GlRptRowRow] = obj["GlRptRow"]
      self.GLRptRowAcct:list[Erp_Tablesets_GLRptRowAcctRow] = obj["GLRptRowAcct"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlRptRowRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.LineNum:int = obj["LineNum"]
      """  Line number  """  
      self.LineType:str = obj["LineType"]
      """   H = Heading Line - Defines a Heading that is printed.
A = Account Details - Prints GL accounts in specified range
S = Summary - a summary of accounts in specified range.
R = Ratio between two rows. 
T = Total - prints a total line for specified total field.  """  
      self.Description:str = obj["Description"]
      """  For LineType H, S and T this description is used to identify the line. For LineType A (acct detail) it is only a reference; the actual description from the GLAcct is used when printing details.  """  
      self.TotalTo:str = obj["TotalTo"]
      """  Defines a field to which the values on this line are accumulated into.  """  
      self.PrintTotal:str = obj["PrintTotal"]
      """  Identifies the "TotalTo"  field that should be printed on this line. Pertains only to Total lines ( LineType = "T" ).  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates if the "signs" of the amounts for this line are to be flipped before they are printed.  """  
      self.NewPage:bool = obj["NewPage"]
      """  New Page flag  """  
      self.SkipBefore:int = obj["SkipBefore"]
      """  # of lines to skip before printing this line.  """  
      self.SkipAfter:int = obj["SkipAfter"]
      """  # of lines to skip after printing this line.  """  
      self.Indents:int = obj["Indents"]
      """  # of spaces that the line will be indented  """  
      self.ClearAfterPrint:bool = obj["ClearAfterPrint"]
      """   Resets the total field defined by "PrintTotal" to zero after printing.
Pertains only to Total lines ( LineType = T ).  """  
      self.TextFont:str = obj["TextFont"]
      """  Override Font that is used for the Text portion of a row. Default is either GLRptCol.DataFont or GLRptMas.ReportFont.  """  
      self.TextFontSize:int = obj["TextFontSize"]
      """  Override Text Font Size used for the Text portion of the row. Default is GLRptCol.DataFontSize or GLRptMas.ReportFontSize.  """  
      self.TextUnderline:str = obj["TextUnderline"]
      """   Underline attribute for the text portion of the line. Default is either GLRptCol.DataUnderLine or GLRptMas.ReportUnderline.
Values: Y = Underline, N = No Underline, "D" = Use default.  """  
      self.TextBold:str = obj["TextBold"]
      """   Bold attribute for the text portion of this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataBold or GLRptMas.ReportBold  """  
      self.TextItalic:str = obj["TextItalic"]
      """   Override Italic attribute for the text portion of this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataItalic or GLRptMas.ReporItalic.  """  
      self.DataFont:str = obj["DataFont"]
      """  Font that is used for ALL the data in this row.  Blank = use default. Default is either GLRptCol.DataFont/GLRptMas.ReportFont.  """  
      self.DataFontSize:int = obj["DataFontSize"]
      """   Override FontSize used for ALL DATA in this line. 0 = Use default.
Default is GLRptCol.DataFontSize/GLRptMas.ReportFontSize.  """  
      self.DataUnderline:str = obj["DataUnderline"]
      """   Underline attribute for ALL DATA in the line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataUnderLine/GLRptMas.ReportUnderline.  """  
      self.DataBold:str = obj["DataBold"]
      """   Bold attribute for ALL DATA on this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataBold/GLRptMas.ReportBold  """  
      self.DataItalic:str = obj["DataItalic"]
      """   Italic attribute for ALL DATA on this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataItalic/GLRptMas.ReporItalic.  """  
      self.RatioLine1:int = obj["RatioLine1"]
      """  The GLRptRow.LineNum that defines the values that are to be used the numerator in the ratio calculation. This only pertains to LineType = "R".  """  
      self.RatioLine2:int = obj["RatioLine2"]
      """  The GLRptRow.LineNum that defines the values that are to be used the denominator in the ratio calculation. This only pertains to LineType = "R".  """  
      self.Category:str = obj["Category"]
      """  Report Category  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text. Only for LineType="T"  """  
      self.ReverseReportCategory:str = obj["ReverseReportCategory"]
      """  ReverseReportCategory  """  
      self.CategoryOrAccounts:str = obj["CategoryOrAccounts"]
      self.COAActCatDescription:str = obj["COAActCatDescription"]
      self.IndentedDescription:str = obj["IndentedDescription"]
      self.PercentCalc:bool = obj["PercentCalc"]
      self.RptCOACode:str = obj["RptCOACode"]
      self.AllowNewAcct:bool = obj["AllowNewAcct"]
      """  Indicates of adding a new specific account is allowed.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ReportIDDescription:str = obj["ReportIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtGlRptMasTableset:
   def __init__(self, obj):
      self.GlRptMas:list[Erp_Tablesets_GlRptMasRow] = obj["GlRptMas"]
      self.GLRptColSet:list[Erp_Tablesets_GLRptColSetRow] = obj["GLRptColSet"]
      self.GLRptCol:list[Erp_Tablesets_GLRptColRow] = obj["GLRptCol"]
      self.GlRptRow:list[Erp_Tablesets_GlRptRowRow] = obj["GlRptRow"]
      self.GLRptRowAcct:list[Erp_Tablesets_GLRptRowAcctRow] = obj["GLRptRowAcct"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportReportDefinition2_input:
   """ Required : 
   reportID
   sFileName
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  ID of the Report Definition to be exported.  """  
      self.sFileName:str = obj["sFileName"]
      """  Desired output file name, optional, no extension required.  """  
      pass

class ExportReportDefinition2_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Exported file subpath of SpecialFolder.UserData.  """  
      pass

class ExportReportDefinition_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  ID of the Report Definition to be exported  """  
      pass

class ExportReportDefinition_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Exported XML Data  """  
      pass

class GetByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlRptMasTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlRptMasTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlRptMasTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name  """  
      self.fieldName:str = obj["fieldName"]
      """  Field Name  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of code destioptions  """  
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
      self.returnObj:list[Erp_Tablesets_GlRptMasListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLRptCol_input:
   """ Required : 
   ds
   reportID
   colSetID
   columnNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      self.reportID:str = obj["reportID"]
      self.colSetID:str = obj["colSetID"]
      self.columnNum:int = obj["columnNum"]
      pass

class GetNewGLRptCol_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLRptRowAcctForType_input:
   """ Required : 
   reportID
   lineNum
   rowAcctType
   ds
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  Report ID  """  
      self.lineNum:int = obj["lineNum"]
      """  Line number  """  
      self.rowAcctType:str = obj["rowAcctType"]
      """  Row account type. Valid types are
            S - Single segment.
            A - Account.  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class GetNewGLRptRowAcctForType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLRptRowAcct_input:
   """ Required : 
   ds
   reportID
   lineNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      self.reportID:str = obj["reportID"]
      self.lineNum:int = obj["lineNum"]
      pass

class GetNewGLRptRowAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGlRptMas_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class GetNewGlRptMas_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGlRptRow_input:
   """ Required : 
   ds
   reportID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      self.reportID:str = obj["reportID"]
      pass

class GetNewGlRptRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGlRptMas
   whereClauseGLRptColSet
   whereClauseGLRptCol
   whereClauseGlRptRow
   whereClauseGLRptRowAcct
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGlRptMas:str = obj["whereClauseGlRptMas"]
      self.whereClauseGLRptColSet:str = obj["whereClauseGLRptColSet"]
      self.whereClauseGLRptCol:str = obj["whereClauseGLRptCol"]
      self.whereClauseGlRptRow:str = obj["whereClauseGlRptRow"]
      self.whereClauseGLRptRowAcct:str = obj["whereClauseGLRptRowAcct"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlRptMasTableset] = obj["returnObj"]
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

class ImportReportDefinition2_input:
   """ Required : 
   sFileSubPath
   newReportID
   overwriteExisting
   """  
   def __init__(self, obj):
      self.sFileSubPath:str = obj["sFileSubPath"]
      """  Imported file subpath of SpecialFolder.UserData.  """  
      self.newReportID:str = obj["newReportID"]
      """  New report ID.  """  
      self.overwriteExisting:bool = obj["overwriteExisting"]
      """  Overwrite existing configurations.  """  
      pass

class ImportReportDefinition2_output:
   def __init__(self, obj):
      pass

class ImportReportDefinition_input:
   """ Required : 
   definitionData
   newReportID
   overwriteExisting
   """  
   def __init__(self, obj):
      self.definitionData:str = obj["definitionData"]
      """  XML Data to be imported  """  
      self.newReportID:str = obj["newReportID"]
      """  New ReportID  """  
      self.overwriteExisting:bool = obj["overwriteExisting"]
      """  Overwrite existing configurations  """  
      pass

class ImportReportDefinition_output:
   def __init__(self, obj):
      pass

class LineTypeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.LineTypeList:str = obj["parameters"]
      pass

      """  output parameters  """  

class MoveGLRptColDown_input:
   """ Required : 
   ColReportID
   ColColSetID
   ColColumnNum
   ColColSetSeq
   ds
   """  
   def __init__(self, obj):
      self.ColReportID:str = obj["ColReportID"]
      """  The report id of the column to move down  """  
      self.ColColSetID:str = obj["ColColSetID"]
      """  The column set id of the column to move down  """  
      self.ColColumnNum:int = obj["ColColumnNum"]
      """  The column number of the column to move down  """  
      self.ColColSetSeq:int = obj["ColColSetSeq"]
      """  The column sequence number of the column to move down  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class MoveGLRptColDown_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MoveGLRptColUp_input:
   """ Required : 
   ColReportID
   ColColSetID
   ColColumnNum
   ColColSetSeq
   ds
   """  
   def __init__(self, obj):
      self.ColReportID:str = obj["ColReportID"]
      """  The report id of the column to move up  """  
      self.ColColSetID:str = obj["ColColSetID"]
      """  The column set id of the column to move up  """  
      self.ColColumnNum:int = obj["ColColumnNum"]
      """  The column number of the column to move up  """  
      self.ColColSetSeq:int = obj["ColColSetSeq"]
      """  The column sequence number of the column to move up  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class MoveGLRptColUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ReportWizardOptionsList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ReportWizardOptionsList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReportWizard_input:
   """ Required : 
   ReportID
   ReportType
   ds
   """  
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      """  The report id to create the template for  """  
      self.ReportType:str = obj["ReportType"]
      """  The type of report to create.
            Valid values are: B (Balance Sheet) or I (Income Statement)  """  
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class ReportWizard_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SyntaxCheckForWeb_input:
   """ Required : 
   CheckReportID
   SyntaxCheckType
   """  
   def __init__(self, obj):
      self.CheckReportID:str = obj["CheckReportID"]
      """  The report id to check the syntax of  """  
      self.SyntaxCheckType:str = obj["SyntaxCheckType"]
      """  The type of syntax check to perform.  Values are:
            I (Income Statment), B (Balance Sheet), or O (Other)  """  
      pass

class SyntaxCheckForWeb_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLRptSyntaxErrorsTableset] = obj["returnObj"]
      pass

class SyntaxCheckOptionsList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.SyntaxCheckOptionsList:str = obj["parameters"]
      pass

      """  output parameters  """  

class SyntaxCheck_input:
   """ Required : 
   CheckReportID
   SyntaxCheckType
   """  
   def __init__(self, obj):
      self.CheckReportID:str = obj["CheckReportID"]
      """  The report id to check the syntax of  """  
      self.SyntaxCheckType:str = obj["SyntaxCheckType"]
      """  The type of syntax check to perform.  Values are:
            I (Income Statment), B (Balance Sheet), or O (Other)  """  
      pass

class SyntaxCheck_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLRptSyntaxErrorsTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlRptMasTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlRptMasTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlRptMasTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateGLRptRow_input:
   """ Required : 
   ReportID
   LineNum
   CategoryOrAccounts
   """  
   def __init__(self, obj):
      self.ReportID:str = obj["ReportID"]
      """  The ReportID of the row  """  
      self.LineNum:int = obj["LineNum"]
      """  The LineNum of the row  """  
      self.CategoryOrAccounts:str = obj["CategoryOrAccounts"]
      """  The CategoryOrAccounts option of the row  """  
      pass

class ValidateGLRptRow_output:
   def __init__(self, obj):
      pass

class ValidateImportedReportDefinition_input:
   """ Required : 
   sFileSubPath
   """  
   def __init__(self, obj):
      self.sFileSubPath:str = obj["sFileSubPath"]
      """  Imported file subpath of SpecialFolder.UserData.  """  
      pass

class ValidateImportedReportDefinition_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Report ID of the imported report definition.  """  
      pass

class YesNoDefaultList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.YesNoDefaultList:str = obj["parameters"]
      pass

      """  output parameters  """  

