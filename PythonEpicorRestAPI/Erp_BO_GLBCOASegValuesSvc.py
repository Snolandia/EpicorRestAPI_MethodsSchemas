import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLBCOASegValuesSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegValues(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBCOASegValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOASegValues
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues",headers=creds) as resp:
           return await resp.json()

async def post_GLBCOASegValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBCOASegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBCOASegValue item
   Description: Calls GetByID to retrieve the GLBCOASegValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBCOASegValue for the service
   Description: Calls UpdateExt to update GLBCOASegValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBCOASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBCOASegValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBCOASegValue item
   Description: Call UpdateExt to delete GLBCOASegValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBCOASegValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_GLBCOASegOpts(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLBCOASegOpts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLBCOASegOpts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegOptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/GLBCOASegOpts",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegValues_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_GLBCOASegOpts_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, SubSegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBCOASegOpt item
   Description: Calls GetByID to retrieve the GLBCOASegOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegOpt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param SubSegmentNbr: Desc: SubSegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBCOASegOptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegValues(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + ")/GLBCOASegOpts(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBCOASegOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBCOASegOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegOptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegOpts",headers=creds) as resp:
           return await resp.json()

async def post_GLBCOASegOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBCOASegOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBCOASegOptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBCOASegOptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBCOASegOpts_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, SubSegmentNbr, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBCOASegOpt item
   Description: Calls GetByID to retrieve the GLBCOASegOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBCOASegOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param SubSegmentNbr: Desc: SubSegmentNbr   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBCOASegOptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegOpts(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBCOASegOpts_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, SubSegmentNbr, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBCOASegOpt for the service
   Description: Calls UpdateExt to update GLBCOASegOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBCOASegOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param SubSegmentNbr: Desc: SubSegmentNbr   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBCOASegOptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegOpts(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBCOASegOpts_Company_ExtCompanyID_COACode_SegmentNbr_SegmentCode_SubSegmentNbr(Company, ExtCompanyID, COACode, SegmentNbr, SegmentCode, SubSegmentNbr, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBCOASegOpt item
   Description: Call UpdateExt to delete GLBCOASegOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBCOASegOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param SegmentNbr: Desc: SegmentNbr   Required: True
      :param SegmentCode: Desc: SegmentCode   Required: True   Allow empty value : True
      :param SubSegmentNbr: Desc: SubSegmentNbr   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/GLBCOASegOpts(" + Company + "," + ExtCompanyID + "," + COACode + "," + SegmentNbr + "," + SegmentCode + "," + SubSegmentNbr + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBCOASegValuesListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLBCOASegValues, whereClauseGLBCOASegOpt, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLBCOASegValues=" + whereClauseGLBCOASegValues
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLBCOASegOpt=" + whereClauseGLBCOASegOpt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(extCompanyID, coACode, segmentNbr, segmentCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
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
   params += "extCompanyID=" + extCompanyID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "coACode=" + coACode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "segmentNbr=" + segmentNbr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "segmentCode=" + segmentCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBCOASegValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBCOASegValues
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBCOASegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBCOASegValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBCOASegValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBCOASegOpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBCOASegOpt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBCOASegOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBCOASegOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBCOASegOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBCOASegValuesSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegOptRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBCOASegOptRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBCOASegValuesListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBCOASegValuesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBCOASegValuesRow] = obj["value"]
      pass

class Erp_Tablesets_GLBCOASegOptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SubSegmentNbr:int = obj["SubSegmentNbr"]
      """  System generated sequence number  """  
      self.ValOption:str = obj["ValOption"]
      """   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  """  
      self.DefaultSegment:str = obj["DefaultSegment"]
      """  Indicates the default segment value to be used for this natural account.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegValuesListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code associated with this segment value and is the ID for the COACurrAcct table.  Only valid for natural accounts (segment 1) where the CurrencyAccount equals Yes.  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the GLBCOASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code associated with this segment value and is the ID for the COACurrAcct table.  Only valid for natural accounts (segment 1) where the CurrencyAccount equals Yes.  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the GLBCOASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  StatUOMCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseCategory:str = obj["ReverseCategory"]
      """  ReverseCategory  """  
      self.ExtAnalysisCode:str = obj["ExtAnalysisCode"]
      """  ExtAnalysisCode  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.GLGainAcctContext:str = obj["GLGainAcctContext"]
      """  GLGainAcctContext  """  
      self.GLLossAcctContext:str = obj["GLLossAcctContext"]
      """  GLLossAcctContext  """  
      self.GainAccount:str = obj["GainAccount"]
      """  GainAccount  """  
      self.LossAccount:str = obj["LossAccount"]
      """  LossAccount  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  AccrualAccount  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
      self.GainSegVal3:str = obj["GainSegVal3"]
      """  GainSegVal3  """  
      self.GainSegVal4:str = obj["GainSegVal4"]
      """  GainSegVal4  """  
      self.GainSegVal5:str = obj["GainSegVal5"]
      """  GainSegVal5  """  
      self.GainSegVal6:str = obj["GainSegVal6"]
      """  GainSegVal6  """  
      self.GainSegVal7:str = obj["GainSegVal7"]
      """  GainSegVal7  """  
      self.GainSegVal8:str = obj["GainSegVal8"]
      """  GainSegVal8  """  
      self.GainSegVal9:str = obj["GainSegVal9"]
      """  GainSegVal9  """  
      self.GainSegVal10:str = obj["GainSegVal10"]
      """  GainSegVal10  """  
      self.GainSegVal11:str = obj["GainSegVal11"]
      """  GainSegVal11  """  
      self.GainSegVal12:str = obj["GainSegVal12"]
      """  GainSegVal12  """  
      self.GainSegVal13:str = obj["GainSegVal13"]
      """  GainSegVal13  """  
      self.GainSegVal14:str = obj["GainSegVal14"]
      """  GainSegVal14  """  
      self.GainSegVal15:str = obj["GainSegVal15"]
      """  GainSegVal15  """  
      self.GainSegVal16:str = obj["GainSegVal16"]
      """  GainSegVal16  """  
      self.GainSegVal17:str = obj["GainSegVal17"]
      """  GainSegVal17  """  
      self.GainSegVal18:str = obj["GainSegVal18"]
      """  GainSegVal18  """  
      self.GainSegVal19:str = obj["GainSegVal19"]
      """  GainSegVal19  """  
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
      self.LossSegVal3:str = obj["LossSegVal3"]
      """  LossSegVal3  """  
      self.LossSegVal4:str = obj["LossSegVal4"]
      """  LossSegVal4  """  
      self.LossSegVal5:str = obj["LossSegVal5"]
      """  LossSegVal5  """  
      self.LossSegVal6:str = obj["LossSegVal6"]
      """  LossSegVal6  """  
      self.LossSegVal7:str = obj["LossSegVal7"]
      """  LossSegVal7  """  
      self.LossSegVal8:str = obj["LossSegVal8"]
      """  LossSegVal8  """  
      self.LossSegVal9:str = obj["LossSegVal9"]
      """  LossSegVal9  """  
      self.LossSegVal10:str = obj["LossSegVal10"]
      """  LossSegVal10  """  
      self.LossSegVal11:str = obj["LossSegVal11"]
      """  LossSegVal11  """  
      self.LossSegVal12:str = obj["LossSegVal12"]
      """  LossSegVal12  """  
      self.LossSegVal13:str = obj["LossSegVal13"]
      """  LossSegVal13  """  
      self.LossSegVal14:str = obj["LossSegVal14"]
      """  LossSegVal14  """  
      self.LossSegVal15:str = obj["LossSegVal15"]
      """  LossSegVal15  """  
      self.LossSegVal16:str = obj["LossSegVal16"]
      """  LossSegVal16  """  
      self.LossSegVal17:str = obj["LossSegVal17"]
      """  LossSegVal17  """  
      self.LossSegVal18:str = obj["LossSegVal18"]
      """  LossSegVal18  """  
      self.LossSegVal19:str = obj["LossSegVal19"]
      """  LossSegVal19  """  
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
      self.AccrualSegVal3:str = obj["AccrualSegVal3"]
      """  AccrualSegVal3  """  
      self.AccrualSegVal4:str = obj["AccrualSegVal4"]
      """  AccrualSegVal4  """  
      self.AccrualSegVal5:str = obj["AccrualSegVal5"]
      """  AccrualSegVal5  """  
      self.AccrualSegVal6:str = obj["AccrualSegVal6"]
      """  AccrualSegVal6  """  
      self.AccrualSegVal7:str = obj["AccrualSegVal7"]
      """  AccrualSegVal7  """  
      self.AccrualSegVal8:str = obj["AccrualSegVal8"]
      """  AccrualSegVal8  """  
      self.AccrualSegVal9:str = obj["AccrualSegVal9"]
      """  AccrualSegVal9  """  
      self.AccrualSegVal10:str = obj["AccrualSegVal10"]
      """  AccrualSegVal10  """  
      self.AccrualSegVal11:str = obj["AccrualSegVal11"]
      """  AccrualSegVal11  """  
      self.AccrualSegVal12:str = obj["AccrualSegVal12"]
      """  AccrualSegVal12  """  
      self.AccrualSegVal13:str = obj["AccrualSegVal13"]
      """  AccrualSegVal13  """  
      self.AccrualSegVal14:str = obj["AccrualSegVal14"]
      """  AccrualSegVal14  """  
      self.AccrualSegVal15:str = obj["AccrualSegVal15"]
      """  AccrualSegVal15  """  
      self.AccrualSegVal16:str = obj["AccrualSegVal16"]
      """  AccrualSegVal16  """  
      self.AccrualSegVal17:str = obj["AccrualSegVal17"]
      """  AccrualSegVal17  """  
      self.AccrualSegVal18:str = obj["AccrualSegVal18"]
      """  AccrualSegVal18  """  
      self.AccrualSegVal19:str = obj["AccrualSegVal19"]
      """  AccrualSegVal19  """  
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.COSegDtlNbr:int = obj["COSegDtlNbr"]
      """  COSegDtlNbr  """  
      self.COPrintBalanceInvDtl:bool = obj["COPrintBalanceInvDtl"]
      """  COPrintBalanceInvDtl  """  
      self.BENAEID:str = obj["BENAEID"]
      """  BENAEID  """  
      self.Mapped:bool = obj["Mapped"]
      """  Mapped  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  ReportCategory  """  
      self.ReverseReportCategory:str = obj["ReverseReportCategory"]
      """  ReverseReportCategory  """  
      self.LinkedPlant:str = obj["LinkedPlant"]
      """  LinkedPlant  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   extCompanyID
   coACode
   segmentNbr
   segmentCode
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.segmentCode:str = obj["segmentCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLBCOASegOptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SubSegmentNbr:int = obj["SubSegmentNbr"]
      """  System generated sequence number  """  
      self.ValOption:str = obj["ValOption"]
      """   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  """  
      self.DefaultSegment:str = obj["DefaultSegment"]
      """  Indicates the default segment value to be used for this natural account.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegValuesListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code associated with this segment value and is the ID for the COACurrAcct table.  Only valid for natural accounts (segment 1) where the CurrencyAccount equals Yes.  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the GLBCOASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegValuesListTableset:
   def __init__(self, obj):
      self.GLBCOASegValuesList:list[Erp_Tablesets_GLBCOASegValuesListRow] = obj["GLBCOASegValuesList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLBCOASegValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  External Company identifier.  Used in Multi-Company Journal.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.SegmentNbr:int = obj["SegmentNbr"]
      """  System generated number from 1 through 20.  """  
      self.SegmentCode:str = obj["SegmentCode"]
      """  Segment value used to construct the GL Account.  """  
      self.SegmentName:str = obj["SegmentName"]
      """  Name of Segment Value  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value.  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active.  Transactions cannot be posted to inactive segments.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used.  It must be less than or equal to the EffectiveTo date.  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used.  It must be greater than or equal to the EffectiveFrom date, if a value was entered in that field.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code associated with this segment value and is the ID for the COACurrAcct table.  Only valid for natural accounts (segment 1) where the CurrencyAccount equals Yes.  """  
      self.CurrAcct:bool = obj["CurrAcct"]
      self.RefEntityType:str = obj["RefEntityType"]
      """  Reference Entity type assigned to this COASegValue.  Only valid when the GLBCOASegment.RefEntity = "GLCOARefType".  """  
      self.Summarization:int = obj["Summarization"]
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  StatUOMCode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReverseCategory:str = obj["ReverseCategory"]
      """  ReverseCategory  """  
      self.ExtAnalysisCode:str = obj["ExtAnalysisCode"]
      """  ExtAnalysisCode  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.GLGainAcctContext:str = obj["GLGainAcctContext"]
      """  GLGainAcctContext  """  
      self.GLLossAcctContext:str = obj["GLLossAcctContext"]
      """  GLLossAcctContext  """  
      self.GainAccount:str = obj["GainAccount"]
      """  GainAccount  """  
      self.LossAccount:str = obj["LossAccount"]
      """  LossAccount  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  AccrualAccount  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
      self.GainSegVal3:str = obj["GainSegVal3"]
      """  GainSegVal3  """  
      self.GainSegVal4:str = obj["GainSegVal4"]
      """  GainSegVal4  """  
      self.GainSegVal5:str = obj["GainSegVal5"]
      """  GainSegVal5  """  
      self.GainSegVal6:str = obj["GainSegVal6"]
      """  GainSegVal6  """  
      self.GainSegVal7:str = obj["GainSegVal7"]
      """  GainSegVal7  """  
      self.GainSegVal8:str = obj["GainSegVal8"]
      """  GainSegVal8  """  
      self.GainSegVal9:str = obj["GainSegVal9"]
      """  GainSegVal9  """  
      self.GainSegVal10:str = obj["GainSegVal10"]
      """  GainSegVal10  """  
      self.GainSegVal11:str = obj["GainSegVal11"]
      """  GainSegVal11  """  
      self.GainSegVal12:str = obj["GainSegVal12"]
      """  GainSegVal12  """  
      self.GainSegVal13:str = obj["GainSegVal13"]
      """  GainSegVal13  """  
      self.GainSegVal14:str = obj["GainSegVal14"]
      """  GainSegVal14  """  
      self.GainSegVal15:str = obj["GainSegVal15"]
      """  GainSegVal15  """  
      self.GainSegVal16:str = obj["GainSegVal16"]
      """  GainSegVal16  """  
      self.GainSegVal17:str = obj["GainSegVal17"]
      """  GainSegVal17  """  
      self.GainSegVal18:str = obj["GainSegVal18"]
      """  GainSegVal18  """  
      self.GainSegVal19:str = obj["GainSegVal19"]
      """  GainSegVal19  """  
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
      self.LossSegVal3:str = obj["LossSegVal3"]
      """  LossSegVal3  """  
      self.LossSegVal4:str = obj["LossSegVal4"]
      """  LossSegVal4  """  
      self.LossSegVal5:str = obj["LossSegVal5"]
      """  LossSegVal5  """  
      self.LossSegVal6:str = obj["LossSegVal6"]
      """  LossSegVal6  """  
      self.LossSegVal7:str = obj["LossSegVal7"]
      """  LossSegVal7  """  
      self.LossSegVal8:str = obj["LossSegVal8"]
      """  LossSegVal8  """  
      self.LossSegVal9:str = obj["LossSegVal9"]
      """  LossSegVal9  """  
      self.LossSegVal10:str = obj["LossSegVal10"]
      """  LossSegVal10  """  
      self.LossSegVal11:str = obj["LossSegVal11"]
      """  LossSegVal11  """  
      self.LossSegVal12:str = obj["LossSegVal12"]
      """  LossSegVal12  """  
      self.LossSegVal13:str = obj["LossSegVal13"]
      """  LossSegVal13  """  
      self.LossSegVal14:str = obj["LossSegVal14"]
      """  LossSegVal14  """  
      self.LossSegVal15:str = obj["LossSegVal15"]
      """  LossSegVal15  """  
      self.LossSegVal16:str = obj["LossSegVal16"]
      """  LossSegVal16  """  
      self.LossSegVal17:str = obj["LossSegVal17"]
      """  LossSegVal17  """  
      self.LossSegVal18:str = obj["LossSegVal18"]
      """  LossSegVal18  """  
      self.LossSegVal19:str = obj["LossSegVal19"]
      """  LossSegVal19  """  
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
      self.AccrualSegVal3:str = obj["AccrualSegVal3"]
      """  AccrualSegVal3  """  
      self.AccrualSegVal4:str = obj["AccrualSegVal4"]
      """  AccrualSegVal4  """  
      self.AccrualSegVal5:str = obj["AccrualSegVal5"]
      """  AccrualSegVal5  """  
      self.AccrualSegVal6:str = obj["AccrualSegVal6"]
      """  AccrualSegVal6  """  
      self.AccrualSegVal7:str = obj["AccrualSegVal7"]
      """  AccrualSegVal7  """  
      self.AccrualSegVal8:str = obj["AccrualSegVal8"]
      """  AccrualSegVal8  """  
      self.AccrualSegVal9:str = obj["AccrualSegVal9"]
      """  AccrualSegVal9  """  
      self.AccrualSegVal10:str = obj["AccrualSegVal10"]
      """  AccrualSegVal10  """  
      self.AccrualSegVal11:str = obj["AccrualSegVal11"]
      """  AccrualSegVal11  """  
      self.AccrualSegVal12:str = obj["AccrualSegVal12"]
      """  AccrualSegVal12  """  
      self.AccrualSegVal13:str = obj["AccrualSegVal13"]
      """  AccrualSegVal13  """  
      self.AccrualSegVal14:str = obj["AccrualSegVal14"]
      """  AccrualSegVal14  """  
      self.AccrualSegVal15:str = obj["AccrualSegVal15"]
      """  AccrualSegVal15  """  
      self.AccrualSegVal16:str = obj["AccrualSegVal16"]
      """  AccrualSegVal16  """  
      self.AccrualSegVal17:str = obj["AccrualSegVal17"]
      """  AccrualSegVal17  """  
      self.AccrualSegVal18:str = obj["AccrualSegVal18"]
      """  AccrualSegVal18  """  
      self.AccrualSegVal19:str = obj["AccrualSegVal19"]
      """  AccrualSegVal19  """  
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.COSegDtlNbr:int = obj["COSegDtlNbr"]
      """  COSegDtlNbr  """  
      self.COPrintBalanceInvDtl:bool = obj["COPrintBalanceInvDtl"]
      """  COPrintBalanceInvDtl  """  
      self.BENAEID:str = obj["BENAEID"]
      """  BENAEID  """  
      self.Mapped:bool = obj["Mapped"]
      """  Mapped  """  
      self.ReportCategory:str = obj["ReportCategory"]
      """  ReportCategory  """  
      self.ReverseReportCategory:str = obj["ReverseReportCategory"]
      """  ReverseReportCategory  """  
      self.LinkedPlant:str = obj["LinkedPlant"]
      """  LinkedPlant  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBCOASegValuesTableset:
   def __init__(self, obj):
      self.GLBCOASegValues:list[Erp_Tablesets_GLBCOASegValuesRow] = obj["GLBCOASegValues"]
      self.GLBCOASegOpt:list[Erp_Tablesets_GLBCOASegOptRow] = obj["GLBCOASegOpt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGLBCOASegValuesTableset:
   def __init__(self, obj):
      self.GLBCOASegValues:list[Erp_Tablesets_GLBCOASegValuesRow] = obj["GLBCOASegValues"]
      self.GLBCOASegOpt:list[Erp_Tablesets_GLBCOASegOptRow] = obj["GLBCOASegOpt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   extCompanyID
   coACode
   segmentNbr
   segmentCode
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.segmentCode:str = obj["segmentCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBCOASegValuesTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBCOASegValuesTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBCOASegValuesTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBCOASegValuesListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLBCOASegOpt_input:
   """ Required : 
   ds
   extCompanyID
   coACode
   segmentNbr
   segmentCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOASegValuesTableset] = obj["ds"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      self.segmentCode:str = obj["segmentCode"]
      pass

class GetNewGLBCOASegOpt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLBCOASegValues_input:
   """ Required : 
   ds
   extCompanyID
   coACode
   segmentNbr
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOASegValuesTableset] = obj["ds"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      self.segmentNbr:int = obj["segmentNbr"]
      pass

class GetNewGLBCOASegValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLBCOASegValues
   whereClauseGLBCOASegOpt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLBCOASegValues:str = obj["whereClauseGLBCOASegValues"]
      self.whereClauseGLBCOASegOpt:str = obj["whereClauseGLBCOASegOpt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBCOASegValuesTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLBCOASegValuesTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLBCOASegValuesTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOASegValuesTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBCOASegValuesTableset] = obj["ds"]
      pass

      """  output parameters  """  

